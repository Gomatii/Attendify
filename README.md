Facial Recognition-Based Attendance System

📌 Overview

This project is a Facial Recognition-Based Attendance System that automates attendance tracking using face detection and recognition. It leverages OpenCV, Flask, MySQL, and TensorFlow to detect and recognize faces, store attendance records in a database, and provide a web-based interface for management.

🚀 Features

✅ Real-time Face Detection & Recognition using OpenCV

✅ Automated Attendance Logging

✅ Web-based Interface using Flask

✅ MySQL Database Integration for storing attendance records

✅ Deep Learning-based Face Recognition (TensorFlow & Keras)

✅ SocketIO for Real-time Communication

🛠️ Technologies Used

🐍 Python

🎥 OpenCV for Face Detection & Recognition

🌐 Flask (Backend & Web Interface)

🔄 Flask-SocketIO for Real-time Communication

🗄️ Flask-MySQLdb for Database Integration

🏛️ MySQL as the Database

🤖 TensorFlow & Keras for Deep Learning-based Face Recognition

📄 CSV Handling for Exporting Attendance Data

🔧 Installation

Prerequisites

Ensure you have Python 3.7+ installed along with the required dependencies.

Step 1: Clone the Repository

 git clone https://github.com/your-username/facial-recognition-attendance.git
 cd facial-recognition-attendance

Step 2: Install Dependencies

 pip install -r requirements.txt

Step 3: Set Up MySQL Database

Create a MySQL database:

CREATE DATABASE attendance_system;

Update database_details.py with your MySQL credentials:

dbhost = "your_host"
dbuser = "your_username"
dbpassword = "your_password"
dbname = "attendance_system"

Run the database migration script (if available) to create necessary tables.

Step 4: Run the Application

 python app.py

Access the web interface at: http://127.0.0.1:5000

📌 Usage

Register Users: Capture and store images of authorized users.

Recognize Faces: The system detects faces from a live camera feed and matches them with stored records.

Mark Attendance: Once a face is recognized, attendance is recorded in the database.

View Attendance Logs: Admin can view and export attendance data.

📁 File Structure

facial-recognition-attendance/
│── app.py                     # Main Flask application
│── database_details.py         # MySQL Database Configurations
│── templates/                  # HTML Templates for Web UI
│── static/                     # CSS & JS files
│── models/                     # Trained Face Recognition Model
│── attendance_from_cam.py      # Capture & Recognize Faces
│── requirements.txt            # Required Python Libraries
└── README.md                   # Documentation

📜 Dependencies

The required dependencies are listed in requirements.txt. Install them using:

pip install -r requirements.txt

🤝 Contributing

Feel free to fork the repository and contribute! Submit a pull request with improvements.

📝 License

This project is open-source under the MIT License.

📧 Contact

For queries or contributions, reach out via [your-email@example.com] or GitHub issues.

