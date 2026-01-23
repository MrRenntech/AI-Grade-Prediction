import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from data_preprocessing import load_and_preprocess

# ------------------------------------------------------------------------------
# 1. Datat Preprocessing
# ------------------------------------------------------------------------------
print("Loading and preprocessing data...")
# Load data and also get the encoders so we can save them for the web app
X, y, encoders = load_and_preprocess("data/student-mat.csv", return_encoders=True)

# Save the label encoders (CRITICAL for consistency in the web app)
# This ensures "Male" is encoded as "1" (or "0") exactly the same way in both training and production
joblib.dump(encoders, "models/encoders.pkl")
print("Encoders saved to models/encoders.pkl")

# Split data into Training and Testing sets
# Stratify=y ensures we have the same ratio of High/Low risk students in both sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------------------------------------------------------------------
# 2. Model 1: Logistic Regression (Baseline)
# ------------------------------------------------------------------------------
print("\nTraining Logistic Regression...")
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_preds = lr.predict(X_test)

# Evaluate Baseline
print("\n--- Logistic Regression Results ---")
print("Accuracy:", accuracy_score(y_test, lr_preds))
print(confusion_matrix(y_test, lr_preds))
print(classification_report(y_test, lr_preds))

# ------------------------------------------------------------------------------
# 3. Model 2: Random Forest (Challenger/Winner)
# ------------------------------------------------------------------------------
print("\nTraining Random Forest...")
rf = RandomForestClassifier(
    n_estimators=200,      # Number of trees
    random_state=42,       # Reproducibility
    class_weight="balanced" # Handle imbalanced risk classes
)
rf.fit(X_train, y_train)
rf_preds = rf.predict(X_test)

# Evaluate Challenger
print("\n--- Random Forest Results ---")
print("Accuracy:", accuracy_score(y_test, rf_preds))
print(confusion_matrix(y_test, rf_preds))
print(classification_report(y_test, rf_preds))

# ------------------------------------------------------------------------------
# 4. Save the Best Model
# ------------------------------------------------------------------------------
# Random Forest typically outperforms Logistic Regression on this dataset
# due to its ability to capture non-linear relationships.
best_model = rf  
joblib.dump(best_model, "models/student_risk_model.pkl")

print("\nBest model (Random Forest) saved to models/student_risk_model.pkl")
