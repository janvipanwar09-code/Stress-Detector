from flask import Flask, render_template, request
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


app = Flask(__name__)


# -----------------------------
# LOAD DATASET
# -----------------------------

DATA_PATH = "SayOPillow.csv"

df = pd.read_csv(DATA_PATH)


# Actual columns in the dataset
features = [
    "sr",
    "rr",
    "t",
    "lm",
    "bo",
    "rem",
    "sr.1",
    "hr"
]

# Stress level column
target = "sl"


# -----------------------------
# STAGE 1
# STRESSED / NOT STRESSED
# -----------------------------

df["stressed"] = df[target].apply(
    lambda x: 1 if x > 0 else 0
)

X = df[features]
y = df["stressed"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

binary_model = LogisticRegression()
binary_model.fit(X_train, y_train)

binary_accuracy = accuracy_score(
    y_test,
    binary_model.predict(X_test)
)


# -----------------------------
# STAGE 2
# STRESS LEVEL 1-4
# -----------------------------

stressed_df = df[df["stressed"] == 1]

X2 = stressed_df[features]
y2 = stressed_df[target]

scaler2 = StandardScaler()
X2_scaled = scaler2.fit_transform(X2)

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2_scaled,
    y2,
    test_size=0.2,
    random_state=42
)

level_model = LogisticRegression(max_iter=1000)
level_model.fit(X2_train, y2_train)

level_accuracy = accuracy_score(
    y2_test,
    level_model.predict(X2_test)
)


# -----------------------------
# HOME PAGE
# -----------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        try:

            values = [
                float(request.form["snoring"]),
                float(request.form["respiration_rate"]),
                float(request.form["body_temp"]),
                float(request.form["limb_movement"]),
                float(request.form["blood_oxygen"]),
                float(request.form["eye_movement"]),
                float(request.form["sleep_hours"]),
                float(request.form["heart_rate"])
            ]

            input_data = np.array(values).reshape(1, -1)

            # Stage 1
            input_scaled = scaler.transform(input_data)

            stress_prediction = binary_model.predict(
                input_scaled
            )[0]

            if stress_prediction == 0:

                result = {
                    "status": "Not Stressed",
                    "level": "No significant stress detected."
                }

            else:

                # Stage 2
                input_scaled_2 = scaler2.transform(input_data)

                stress_level = level_model.predict(
                    input_scaled_2
                )[0]

                result = {
                    "status": "Stress Detected",
                    "level": f"Stress Level: {stress_level} / 4"
                }

        except Exception as e:

            result = {
                "status": "Error",
                "level": str(e)
            }

    return render_template(
        "index.html",
        result=result
    )


# -----------------------------
# RUN APPLICATION
# -----------------------------

if __name__ == "__main__":
    app.run(debug=True)
   



