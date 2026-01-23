import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import sys
import os

# Add the current directory to sys.path to ensure we can import the module if run from src or root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sgpa_preprocessing import load_sgpa_data

# Adjust path to data if running from src or root
data_path = "data/student-mat.csv"
if not os.path.exists(data_path):
    # Try looking one level up if we are in src
    data_path = "../data/student-mat.csv"

try:
    X, y, scaler = load_sgpa_data(data_path)
except FileNotFoundError:
    print(f"Error: Could not find data file at {data_path}")
    sys.exit(1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)
preds = model.predict(X_test)

print("SGPA Band Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))

# Ensure models directory exists
models_dir = "models"
if not os.path.exists(models_dir):
     # Try looking one level up if we are in src
    if os.path.exists("../models"):
        models_dir = "../models"
    else:
        os.makedirs(models_dir)

joblib.dump(model, os.path.join(models_dir, "sgpa_band_model.pkl"))
joblib.dump(scaler, os.path.join(models_dir, "sgpa_scaler.pkl"))

print("SGPA model and scaler saved.")
