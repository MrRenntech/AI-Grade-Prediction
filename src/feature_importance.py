import joblib
import pandas as pd
import matplotlib.pyplot as plt

from data_preprocessing import load_and_preprocess

# Load data
print("Loading Data...")
X, y = load_and_preprocess("data/student-mat.csv")

# Load trained model
print("Loading Model...")
model = joblib.load("models/student_risk_model.pkl")

# Extract feature importance
importances = model.feature_importances_
features = X.columns

fi_df = pd.DataFrame({
    "Feature": features,
    "Importance": importances
}).sort_values(by="Importance", ascending=False).head(10)

# Plot
plt.figure(figsize=(8, 5))
plt.barh(fi_df["Feature"], fi_df["Importance"])
plt.gca().invert_yaxis()
plt.xlabel("Importance Score")
plt.title("Top Features Influencing Student Risk")
plt.tight_layout()

# Save plot
plt.savefig("models/feature_importance.png")
print("\nFeature Importance Plot saved to models/feature_importance.png")
# plt.show() # Commented out for non-interactive environments

print("\nTop Risk-Contributing Features:")
print(fi_df)
