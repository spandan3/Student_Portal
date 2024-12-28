# ONLINE STUDENT PORTAL - Project by Spandan

## Description:

I have made a Student Portal which is easy, useful and accessible. The biggest advantage of the portal lies in its ability to enhance efficiency by reducing the reliance on manual human effort, while simultaneously serving as a medium for paper conservation, carbon footprint reduction, and most importantly - for saving time of educators and students.


## Project Overview:

Creating an Optimized Student Portal: Each student has their own portal with personal certificates, photos, an event planner, and attendance reports conveniently accessible in one place.

Integrating AI for efficiency: AI-powered face recognition automates photo uploads and digital attendance tracking. Additionally, AI-driven certificate scanning ensures accurate and rapid certificate uploads, making the system both time-saving and environmentally conscious.

Fostering Sustainability: By digitizing processes, its reducing paper and resource waste, minimizing carbon footprints.
I also plan to promote eco-friendly practices in students through our 'Sustainable Tip of the Day' feature in the portal.

## Description of Each Module:

### Attendance Module:
<p>A webcam/camera is set up to mark the attendance. <br>
The program (attendance.py) runs and matches each face detected in the camera to the profile pictures of the student. <br>
The faces that are matched are then linked to the corresponding student’s profile <br>
Hence the exact date and time when the attendance is marked is uploaded to the MySQL database as well as the student portal.<br>
</p>

### Photo Module:
<p>All the Photos are uploaded to one central folder. <br>
The program (facerecog.py) runs and loads the pictures from that folder and matches each face detected in the photos to the profile pictures of the student. <br>
These sorted photos are then linked to the corresponding  student’s profile <br>
The photos are then uploaded to the MySQL database as well as student portal and the student can view them at any time.<br>
</p>


### Certificates Module:
<p>All the Certificates are uploaded to one central folder. <br>
First (filenames.py) is run to load the filename of each certificate into a single .txt file <br>
Then (certificatesort.py) is run to load the text from each certificate, sort through it and find the name corresponding to the certificate <br>
These certificates along with the corresponding student name are then uploaded to the MySQL database as well as the student portal.<br>
</p>


### Event Planner Module:
<p>All the event information is stored in a MySQL database. <br>
Students have the option to add and delete their own events.<br>
These changes are updated accordingly in the MySQL database and hence the unique events are saved for each student (events are linked with their student ID).<br>
</p>

## Software Used:

<p>I have used HTML, CSS and Flask for the website frontend.<br>
Python and its modules like face_recognition, OpenCV, PyPDF2 are used to make the code for the functionality of each module in the portal. <br>
Finally, I have used MySQL DBMS to save the information of each student consisting of their login information, filename of their pictures, certificates, attendance and events which all corresponds to the student's unique GR Number (Unique ID).</p>


### Please note: All the required tables must be created in the MySQL database. Refer to [MySQL Tables](./MySQL_Tables.md) for details on all the tables. <br> <br>Refer to the [Student Portal presentation](./Presentation.pdf) for more information.