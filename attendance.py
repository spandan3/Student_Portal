import cv2
import face_recognition
from datetime import datetime
import mysql.connector
import os

# Run this file to open up the webcam and log attendance of all students into the MySQL table along with their names.

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hackathon"
)
cursor = db.cursor()


def mark_attendance(name, frame):
    now = datetime.now()
    date_time = now.strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute("INSERT INTO attendance (name, date_time) VALUES (%s, %s)", (name, date_time))
    db.commit()

known_faces = []
known_names = []
for file in os.listdir('./static/Face/Profile Photos'):
    name = os.path.splitext(file)[0]
    image_path = os.path.join('./static/Face/Profile Photos', file)
    img = face_recognition.load_image_file(image_path)
    face_encoding = face_recognition.face_encodings(img)[0]
    known_faces.append(face_encoding)
    known_names.append(name)

# Webcam
cap = cv2.VideoCapture(0)

marked_names = set()

while True:
    ret, frame = cap.read()
    
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    tolerance = 0.4
    
    for face_encoding, face_location in zip(face_encodings, face_locations):
        top, right, bottom, left = face_location

        matches = face_recognition.compare_faces(known_faces, face_encoding, tolerance)
        name = "Unknown"
        
        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
        
        if name != "Unknown" and name not in marked_names:
            mark_attendance(name, frame)
            marked_names.add(name)
    
    cv2.imshow('Video', frame)
    
    # Click 'q' to end program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
db.close()
