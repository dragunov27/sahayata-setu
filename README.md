# sahayata-setu
🩺 Sahayata Setu – Healthcare Support Interface

Sahayata Setu is a small web application made using Flask, HTML, Tailwind CSS, and JavaScript.
It allows patients to request help and volunteers to register their skills.
The system gives a basic AI-style analysis based on keywords.

This project is mainly for learning and demo purposes.

✨ Features

Patient can submit health related issues

Volunteer can register skills (doctor, driver, counselor, etc.)

Simple keyword based analysis

Shows urgency level for patients

Assigns team and badge for volunteers

Clean and minimal UI

Beginner friendly Flask backend

🛠️ Tech Stack

Backend: Python (Flask)

Frontend: HTML, Tailwind CSS

Logic: JavaScript + Python

API: JSON based POST request

📁 Project Structure
project-folder/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── (optional)
└── README.md

🚀 How to Run the Project
1️⃣ Install Python (if not installed)

Make sure Python 3 is installed.

python --version

2️⃣ Install Flask
pip install flask

3️⃣ Run the Flask App
python app.py


You should see something like:

Running on http://127.0.0.1:5000/

4️⃣ Open in Browser

Open your browser and go to:

http://127.0.0.1:5000/

🧠 How It Works (Simple Explanation)
👤 Patient Mode

User selects Patient

Enters their problem

System checks keywords like:

emergency, pain, bleeding → High urgency

fever, appointment → Medium urgency

Displays:

Category (Medical, Mental Health, Logistics)

Urgency level

Auto response message

🤝 Volunteer Mode

User selects Volunteer

Enters skills

System checks keywords like:

doctor, nurse → Medical Team

car, drive → Transport Team

talk, listen → Counseling Team

Displays:

Assigned team

Skill badge

Welcome message

⚠️ Disclaimer

This is not a real medical system

No real AI or ML is used

Only keyword matching

Do not use for real emergencies

📌 Future Improvements (Optional)

Database support

Login system

Real AI / ML model

Admin dashboard

SMS / Email notifications
