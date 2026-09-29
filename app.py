from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)


# -----------------------------
# DATASET PATH
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "SayOPillow.csv")


# -----------------------------
# FEATURES
# -----------------------------

FEATURES = [
    "sr",
    "rr",
    "t",
    "lm",
    "bo",
    "rem",
    "sr.1",
    "hr"
]


# -----------------------------
# LOAD MODEL
# -----------------------------

def train_model():

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            "SayOPillow.csv was not found in the project folder."
        )

    df = pd.read_csv(DATA_PATH)

    X = df[FEATURES]
    y = df["sl"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = LogisticRegression(
        max_iter=2000,
        random_state=42
    )

    model.fit(X_scaled, y)

    return model, scaler


# -----------------------------
# HOME PAGE
# -----------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    error = None

    if request.method == "POST":

        try:

            values = []

            for feature in FEATURES:

                value = request.form.get(feature)

                if value is None or value.strip() == "":
                    raise ValueError(
                        f"Missing value for {feature}"
                    )

                values.append(float(value))

            model, scaler = train_model()

            input_data = np.array(values).reshape(1, -1)

            input_scaled = scaler.transform(input_data)

            result = model.predict(input_scaled)[0]

            stress_levels = {
                0: "Low Stress",
                1: "Mild Stress",
                2: "Moderate Stress",
                3: "High Stress",
                4: "Very High Stress"
            }

            prediction = stress_levels.get(
                int(result),
                f"Stress Level {int(result)}"
            )

        except Exception as e:

            error = str(e)

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


# -----------------------------
# VERCEL ENTRY POINT
# -----------------------------

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
   






                
