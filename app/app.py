from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import sys
import os

# Add src to path to allow imports from sibling directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data_preprocessing import load_and_preprocess
from src.risk_scoring import risk_scoring

app = Flask(__name__)

# Load model once at startup
MODEL_PATH = "models/student_risk_model.pkl"
model = joblib.load(MODEL_PATH)

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

        response = {
            "prediction": prediction,
            "probabilities": {
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
