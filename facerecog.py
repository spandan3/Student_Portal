import face_recognition
import os
import mysql.connector
import cv2
import time

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hackathon"
)

# Run this file to add the path of the pictures of all the students to the MySQL table along with their corresponding unique student number.

cursor = db.cursor()
cursor.execute("DELETE FROM detected_faces")
db.commit()


def save_to_database(name, image_path, base_path):
    
    student = os.path.basename(name).replace('.jpg', '')
    relative_path = image_path.replace(base_path, '')
    relative_path = relative_path.replace("\\", "/")
    new_path = "Face/Group Photos" + relative_path
    
    cursor.execute("INSERT INTO detected_faces (name, image_path) VALUES (%s, %s)", (student, new_path))
    db.commit()


def detect_and_insert_matches(profiles_folder, group_photos_folder, tolerance=0.4):
    start_time = time.time()
    for subdir, dirs, files in os.walk(group_photos_folder):
        for file in files:
            img_path = os.path.join(subdir, file)
            group_image = face_recognition.load_image_file(img_path)
            group_face_encodings = face_recognition.face_encodings(group_image)
            
            for profile_subdir, _, profile_files in os.walk(profiles_folder):
                for profile_file in profile_files:
                    profile_img_path = os.path.join(profile_subdir, profile_file)
                    profile_image = face_recognition.load_image_file(profile_img_path)
                    profile_face_encodings = face_recognition.face_encodings(profile_image)
                    
                    if not profile_face_encodings:
                        continue  
                    
                    for (top, right, bottom, left) in face_recognition.face_locations(group_image):
                        face_encoding = face_recognition.face_encodings(group_image, [(top, right, bottom, left)])[0]
                        
                        for profile_encoding in profile_face_encodings:
                            match = face_recognition.compare_faces([profile_encoding], face_encoding, tolerance=0.5)
                            if match[0]:
                                save_to_database(profile_img_path, img_path, group_photos_folder)

                                
                                # Draw a rectangle around the matching face in the group photo
                                # cv2.rectangle(group_image, (left, top), (right, bottom), (0, 255, 0), 2)
                                break

                    # Save the modified group photo with rectangles
                    # img_with_rectangles_path = os.path.join(subdir, "annotated_" + file)
                    # cv2.imwrite(img_with_rectangles_path, group_image)
    
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time} seconds")

profiles_folder = "./static/Face/Profile Photos"
group_photos_folder = "./static/Face/Group Photos"
detect_and_insert_matches(profiles_folder, group_photos_folder)

db.close()
