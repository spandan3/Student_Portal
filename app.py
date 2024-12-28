from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import mysql.connector
from datetime import datetime

# Flask App
app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Hackathon2023'  

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="hackathon",
    charset='utf8' # Encoding system for unicode
)

cursor = db.cursor()

def get_random_tip():
    cursor.execute("SELECT tip_text FROM tipofday ORDER BY RAND() LIMIT 1")
    tip = cursor.fetchone()
    return tip[0] if tip else "No tips available."

@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT GRNo FROM users WHERE username = %s AND password = %s", (username, password))
        user_grno = cursor.fetchone()

        if user_grno:
            session['user_id'] = user_grno[0]  
            return redirect(url_for('portal'))  
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')


@app.route('/portal')
def portal():
    if 'user_id' in session:
        user_grno = session['user_id']

        cursor.execute("SELECT Name FROM students WHERE GRNo = %s", (user_grno,))
        result = cursor.fetchone()

        if result:
            student_name = result[0]
            tip = get_random_tip()
            
            session['tip_of_the_day'] = tip
            return render_template('portal.html', student_name=student_name)
        else:
            return "Student not found in the database."
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out', 'info')
    return redirect(url_for('login'))

@app.route('/attendance')
def attendance():
    if 'user_id' in session:
        user_grno = session['user_id']
        dates = []
        times = []

        cursor.execute("SELECT date_time FROM attendance WHERE name = (SELECT Name FROM students WHERE GRNo = %s) order by date_time desc", (user_grno,))
        attendance_records = cursor.fetchall()

        for record in attendance_records:
            date_time = record[0].strftime("%Y-%m-%d %H:%M:%S") 
            date, time = date_time.split()
            dates.append(date)
            times.append(time)

        return render_template('attendance.html', dates=dates, times=times)
    else:
        return redirect(url_for('login'))




@app.route('/photos')
def photos():
    if 'user_id' in session:
        user_grno = session['user_id']

        cursor.execute("SELECT Name FROM students WHERE GRNo = %s", (user_grno,))
        result = cursor.fetchone()

        if result:
            student_name = result[0]

            cursor.execute("SELECT image_path FROM detected_faces WHERE name = %s", (student_name,))
            images = [image[0] for image in cursor.fetchall()]

            return render_template('photos.html', student_name=student_name, images=images)
        else:
            return "Student not found in the database."
    else:
        return redirect(url_for('login'))


@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/certificates')
def certificates():
    if 'user_id' in session:
        user_grno = session['user_id']

        cursor.execute("SELECT Name FROM students WHERE GRNo = %s", (user_grno,))
        result = cursor.fetchone()

        if result:
            student_name = result[0]

            cursor.execute("SELECT filename FROM files WHERE Name = %s", (student_name,))
            certificates = [certificate[0] for certificate in cursor.fetchall()]

            return render_template('certificates.html', student_name=student_name, certificates=certificates)
        else:
            return "Student not found in the database."
    else:
        return redirect(url_for('login'))

@app.route('/add_event', methods=['POST'])
def add_event():
    if 'user_id' in session:
        user_grno = session['user_id']

        event_date = request.form['event_date']
        event_description = request.form['event_description']

        cursor.execute("INSERT INTO events (GRNo, event_date, event_description) VALUES (%s, %s, %s)",
                       (user_grno, event_date, event_description))
        db.commit()

        if cursor.rowcount > 0:
            return 'Event added successfully', 200
        else:
            return 'Error adding event', 400
    else:
        return 'Unauthorized', 401


@app.route('/delete_event', methods=['POST'])
def delete_event():
    if 'user_id' in session:
        user_grno = session['user_id']

        data = request.get_json()
        date_to_delete = data.get('date')
        description_to_delete = data.get('description')

        cursor.execute("DELETE FROM events WHERE GRNo = %s AND event_date = %s AND event_description = %s",
                       (user_grno, date_to_delete, description_to_delete))
        db.commit()

        if cursor.rowcount > 0:
            return 'Event deleted successfully', 200
        else:
            return 'Error deleting event', 400
    else:
        return 'Unauthorized', 401


@app.route('/get_events', methods=['GET'])
def get_events():
    if 'user_id' in session:
        user_grno = session['user_id']

        cursor.execute("SELECT event_date, event_description FROM events WHERE GRNo = %s", (user_grno,))
        events = cursor.fetchall()

        # list of events in JSON format
        event_list = [{'date': str(event[0]), 'description': event[1]} for event in events]

        return jsonify(events=event_list)
    else:
        return jsonify(events=[])




if __name__ == '__main__':
    app.run(debug=True)
