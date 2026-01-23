
# 🛠️ How to Run the Student Performance AI Project

> [!NOTE]
> This application is optimized for the **Brave Browser** for the best visual experience and privacy.

## 📋 Prerequisites
1.  **Python 3.8+** installed.
2.  **Brave Browser** installed (recommended).
3.  Ensure you are in the project root directory: `student-performance-ai`

## ⚙️ Setup

### 1. Create a Virtual Environment (Optional but Recommended)
```bash
# Create venv
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🏃 Running the Pipeline
The project consists of three main stages: Data Loading, Training, and Evaluation.

### 1. 🧠 Train the Model
Run the training script to load data, preprocess it, train the models (Logistic Regression & Random Forest), and save the best one.

**Command:**
```bash
python src/train_model.py
```

**Output:**
- 📈 Prints accuracy scores.
- 💾 Saves the best model to `models/student_risk_model.pkl`.

### 2. 📊 Evaluate & Analyze
Run the evaluation script to generate detailed metrics, plots, and feature importance.

**Command:**
```bash
python src/evaluate_model.py
python src/feature_importance.py
```

**Output:**
- Prints Classification Report and Confusion Matrix.
- Calculates ROC-AUC score.
- Saves plots to `models/roc_curve.png` and `models/feature_importance.png`.

---

## 🌐 3. Run the Web App (Prediction System)
Start the Flask web application to use the model via a web interface.

**Command:**
```bash
python app/app.py
```

**Usage:**
- Open browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- Enter student details to get a risk prediction.

### File Structure Overview
- `src/`: Core logic for training and evaluation.
- `app/`: Flask web application.
- `data/`: Datasets (`student-mat.csv`).
- `models/`: Trained models (`.pkl`) and plots (`.png`).

---

## 🚀 4. Run the Executable (Standalone)
Run the packaged application without needing Python installed.

**Location:** `dist/student_risk_predictor.exe`

**Usage:**
1.  Double-click the executable.
2.  It will start a local server.
3.  Access [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
