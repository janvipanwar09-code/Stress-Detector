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
├── app.py
├── SayOPillow.csv
└── requirements.txt

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/janvipanwar09-code/Stress-Detector.git
cd Stress-Detector

### 2. Install dependencies
```bash
pip install -r requirements.txt

### 3. Run the application
```bash
python app.py

### 4.Open in your browser 
```bash
http://127.0.0.1:5000

🎯 Project Purpose

This project demonstrates how Machine Learning and Flask can be used to build a web-based stress detection system using physiological and sleep-related data.

⚠️ Disclaimer

This project is created for educational and demonstration purposes. It is not intended for medical diagnosis or to replace professional medical advice.

👩‍💻 Author

Janvi Panwar

BCA Graduate | Python | SQL | Data Analytics | AI & Generative AI


