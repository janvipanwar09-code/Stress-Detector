# 🧠 Smart Stress Detector

A machine learning-based web application that detects stress and predicts the stress level using sleep and physiological parameters.

## 🚀 Features

- Stress detection using Machine Learning
- Stress level prediction from 0 to 4
- Uses multiple physiological and sleep-related parameters
- Flask-based web application
- Simple and responsive user interface
- Real-time prediction through a web form

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Logistic Regression
- HTML5
- CSS3
- Bootstrap 5

## 🧠 Machine Learning

The application uses machine learning to analyze the following parameters:

- Snoring
- Respiration Rate
- Body Temperature
- Limb Movement
- Blood Oxygen
- Eye Movement
- Sleep Duration
- Heart Rate

The prediction process works in two stages:

1. **Stress Detection** – Determines whether stress is detected.
2. **Stress Level Prediction** – Predicts the stress level from 1 to 4 when stress is detected.

## 📊 Dataset

The project uses the `SayOPillow.csv` dataset.

The dataset contains sleep and physiological parameters used for training the machine learning models.

## 📁 Project Structure

```text
Stress-Detector/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
⚙️ Installation
1. Clone the repository
git clone https://github.com/janvipanwar09-code/Stress-Detector.git
2. Open the project folder
cd Stress-Detector
3. Install dependencies
pip install -r requirements.txt
4. Run the application
python app.py
5. Open the application

Open:

http://127.0.0.1:5000
🎯 Project Purpose

This project demonstrates the use of machine learning and Flask to build a web-based stress detection system using sleep and physiological data.

⚠️ Disclaimer

This project is created for educational and demonstration purposes. It is not intended to provide medical diagnosis or replace professional medical advice.

👩‍💻 Author

Janvi Panwar

BCA Graduate | Python | SQL | Data Analytics | AI & Generative AI


**Bas poora paste karo → Commit changes.** ❤️

Screenshot abhi README mein nahi daal rahe; pehle README properly save kar lete hain.
├── app.py
├── SayOPillow.csv
└── requirements.txt
