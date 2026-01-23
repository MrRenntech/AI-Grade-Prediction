import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve,
    auc
)
from data_preprocessing import load_and_preprocess

# ------------------------------------------------------------------------------
# 1. Load Data and Model
# ------------------------------------------------------------------------------
print("Loading data for evaluation...")
X, y = load_and_preprocess("data/student-mat.csv")

# Recreate the exact same split as training to ensure we evaluate on the Test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Loading trained model...")
model = joblib.load("models/student_risk_model.pkl")

# ------------------------------------------------------------------------------
# 2. Generate Predictions
# ------------------------------------------------------------------------------
y_pred = model.predict(X_test)        # Class predictions (0, 1, 2)
y_prob = model.predict_proba(X_test)  # Probabilities for ROC

# ------------------------------------------------------------------------------
# 3. Print Metrics
# ------------------------------------------------------------------------------
print("\n--- Classification Report ---")
print(classification_report(y_test, y_pred))

print("\n--- Confusion Matrix ---")
print(confusion_matrix(y_test, y_pred))

# Calculate ROC-AUC Score (Macro-average for multiclass)
roc_auc = roc_auc_score(y_test, y_prob, multi_class="ovr")
print("\nROC-AUC Score (OVR):", roc_auc)

# ------------------------------------------------------------------------------
# 4. Plot Multiclass ROC Curve
# ------------------------------------------------------------------------------
print("generating ROC curve...")

# Binarize the output for Multiclass ROC plotting
lb = LabelBinarizer()
lb.fit(y)
y_test_bin = lb.transform(y_test)

n_classes = y_test_bin.shape[1]
colors = ['blue', 'red', 'green']
class_names = ['Low Risk', 'Medium Risk', 'High Risk'] # Assuming 0, 1, 2 map to this

plt.figure(figsize=(10, 6))
for i in range(n_classes):
    fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_prob[:, i])
    roc_auc_class = auc(fpr, tpr)
    plt.plot(fpr, tpr, color=colors[i % len(colors)], lw=2,
             label=f'Class {i} ({class_names[i]}) (area = {roc_auc_class:.2f})')

plt.plot([0, 1], [0, 1], 'k--', lw=2) # Diagonal line
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve - Student Risk Prediction (Multiclass)')
plt.legend(loc="lower right")

# Save plot instead of showing (better for non-interactive envs)
plt.savefig("models/roc_curve.png")
print("\nROC Curve saved to models/roc_curve.png")
