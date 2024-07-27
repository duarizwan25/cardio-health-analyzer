# Medical Magic: Disease Identifier and Health Management System

## Project Overview

Medical Magic is an integrated health management system designed to help users manage their health profiles, identify potential diseases based on symptoms, and receive prescriptions. The system features a user-friendly interface built with Tkinter and offers functionalities such as a symptom checker, prescription emailer, and health monitoring dashboard. Additionally, it provides a chatbot interface for user interaction and a calendar for scheduling.

## Features

1. **Patient Profile Management**:
   - Input patient information including name, age, gender, weight, and height.
   - Validate user input for correctness.
   - Store patient data in a CSV file for record-keeping.

2. **Symptom Checker and Disease Identifier**:
   - Select symptoms from a predefined list associated with various diseases.
   - Identify potential diseases based on selected symptoms.
   - Display matching diseases and provide relevant prescriptions.

3. **Prescription Emailer**:
   - Generate and send prescriptions via email using SMTP.
   - Integrate prescription details with patient email for easy access.

4. **User Interface**:
   - Multi-page interface with transitions between profile setup, symptom checker, and prescription pages.
   - Use of Tkinter and PIL for graphical elements and layout.
   - Responsive design with validation and error handling.

5. **Health Monitoring Dashboard**:
   - Visual representation of health metrics such as blood pressure, heart rate, blood count, and glucose levels.
   - Easy navigation through a sidebar menu.

6. **Chatbot Integration**:
   - Redirect users to a chatbot interface for interactive support and inquiries.

7. **Calendar Integration**:
   - Calendar widget for scheduling and viewing appointments.

## Installation and Setup

1. **Dependencies**:
   - Python 3.x
   - Tkinter
   - Pillow (PIL)
   - smtplib
   - tkcalendar

2. **File Structure**:
   ```
   MedicalMagic/
   ├── main.py
   ├── Cardio Health Analyzer.py
   ├── reports.py
   ├── chatbot.py
   ├── images/
   │   ├── pg1.jpg
   │   ├── pg2.jpg
   │   ├── 4thpage.png
   │   ├── bg.jpeg
   │   ├── heart.png
   ├── data/
   │   ├── hospital_record.csv
   │   ├── prescription.txt
   │   ├── data.txt
   ├── Textfiles/
   │   ├── Heart.txt
   │   ├── Valve.txt
   │   ├── Vein.txt
   │   ├── Stroke.txt
   │   ├── Rhythm.txt
   │   ├── ALHAMDULLILAH!.txt
   ├── README.md
   └── requirements.txt
   ```

3. **Running the Application**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Run the main script: `python main.py`
   - Follow the on-screen instructions to navigate through the application.

## Usage

1. **Patient Profile**:
   - Start by entering the patient’s name, age, gender, weight, and height.
   - Click "Done" to save the profile and proceed to symptom checking.

2. **Symptom Checker**:
   - Select symptoms from the list provided.
   - Click "Identify Disease" to get a diagnosis based on selected symptoms.
   - View the potential diseases and the corresponding prescriptions.

3. **Send Prescription**:
   - Enter the patient’s email address.
   - Click "Send Prescription" to email the prescription.

4. **Dashboard and Additional Features**:
   - Navigate using the sidebar to access the dashboard, reports, calendar, and chatbot.

## Contributing

Contributions to the project are welcome. Please fork the repository and submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact

For any questions or support, please contact the project maintainer at [hospitalour6@gmail.com](mailto:hospitalour6@gmail.com).
