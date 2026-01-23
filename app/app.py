from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import numpy as np
import sys
import os

from src.cgpa_projection import project_cgpa

# Add src to path to allow imports from sibling directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data_preprocessing import load_and_preprocess
from src.risk_scoring import risk_scoring

app = Flask(__name__)

# Load model once at startup
MODEL_PATH = "models/student_risk_model.pkl"
SGPA_MODEL_PATH = "models/sgpa_band_model.pkl"
SGPA_SCALER_PATH = "models/sgpa_scaler.pkl"

model = joblib.load(MODEL_PATH)
sgpa_model = joblib.load(SGPA_MODEL_PATH)
sgpa_scaler = joblib.load(SGPA_SCALER_PATH)

SGPA_BAND_MAP = {
    0: (0.0, 6.0),
    1: (6.0, 7.0),
    2: (7.0, 8.0),
    3: (8.0, 9.0),
    4: (9.0, 10.0)
}

SGPA_REPRESENTATIVE = {
    0: 5.5,
    1: 6.5,
    2: 7.5,
    3: 8.5,
    4: 9.25
}

# Load column structure for consistency
# Note: This relies on data_preprocessing returning X which has columns
# Since data_preprocessing.py in this project returns separate X (with columns) and y,
# we need to unpack the return value.
# load_and_preprocess signature: (path, return_encoders=False) -> X, y OR X, y, encoders
# We call it with default args -> X, y
X_sample, _ = load_and_preprocess("data/student-mat.csv")
FEATURE_COLUMNS = X_sample.columns.tolist()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Manual Feature Engineering to match model training
        if 'G1_G2_AVG' in data:
            avg_grade = data.pop('G1_G2_AVG')
            data['G1'] = avg_grade
            data['G2'] = avg_grade

        # Convert input to DataFrame
        input_df = pd.DataFrame([data])

        # Ensure column order
        # fill_value=0 is critical here because the payload might be missing columns
        input_df = input_df.reindex(columns=FEATURE_COLUMNS, fill_value=0)

        # Predict
        probabilities = model.predict_proba(input_df)[0]
        prediction = risk_scoring(probabilities)

        # ---------------------------
        # SGPA PREDICTION
        # ---------------------------
        # SGPA model requires G1_G2_AVG and NO G1/G2
        # Input_df has G1/G2 (from Risk Schema).
        sgpa_input_df = input_df.copy()
        
        # Calculate AVG (Assuming G1 and G2 are present and numeric)
        sgpa_input_df['G1_G2_AVG'] = (sgpa_input_df['G1'] + sgpa_input_df['G2']) / 2
        
        # Drop G1 and G2
        sgpa_input_df = sgpa_input_df.drop(columns=['G1', 'G2'])

        sgpa_features = sgpa_input_df.values
        sgpa_features_scaled = sgpa_scaler.transform(sgpa_features)

        sgpa_band = int(sgpa_model.predict(sgpa_features_scaled)[0])
        sgpa_range = SGPA_BAND_MAP[sgpa_band]
        predicted_sgpa_value = SGPA_REPRESENTATIVE[sgpa_band]

        # ---------------------------
        # CGPA PROJECTION
        # ---------------------------
        current_cgpa = float(data.get("current_cgpa", 0))
        completed_semesters = int(data.get("completed_semesters", 0))

        projected_cgpa = project_cgpa(
            current_cgpa,
            completed_semesters,
            predicted_sgpa_value
        )

        response = {
            "risk_assessment": prediction,

            "academic_prediction": {
                "predicted_sgpa_range": f"{sgpa_range[0]} – {sgpa_range[1]}",
                "projected_cgpa": projected_cgpa
            },

            "model_probabilities": {
                "low_risk": round(probabilities[0], 3),
                "medium_risk": round(probabilities[1], 3),
                "high_risk": round(probabilities[2], 3)
            }
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
