![Student Performance AI Banner](assets/banner.png)

# 🎓 AI Grade Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?style=for-the-badge&logo=flask&logoColor=white)
![Sklearn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Complete-success?style=for-the-badge)

**An intelligent, data-driven system to predict student academic risk using Machine Learning.**  
*Empowering educators with early warning signals to improve student success rates.*

---

## 🚀 Key Features

*   **📊 Predictive Analytics**: Utilizes **Random Forest** (91% Accuracy) to classify students into Low, Medium, or High risk categories.
*   **🔮 Academic Forecasting**: Predicts future **SGPA Bands** and projects **CGPA** using deterministic academic logic.
*   **🧠 Intelligent Scoring**: Generates a precise **Risk Score** and **Confidence Level** for actionable insights.
*   **🎨 Professional Interface**: A clean, academic dashboard designed for decision support.
*   **📦 Portable Deployment**: Fully packaged standalone `.exe` for instant use on any Windows machine.
*   **📈 Explainable AI**: Visualizes key risk drivers like Study Time, Absences, and Past Class Failures.

---

## 🏗️ System Architecture

```mermaid
graph LR
    User[User / Educator] -->|Inputs Data| FE[Frontend Interface]
    FE -->|POST Request| API[Flask API]
    subgraph "Backend Processing"
        API -->|Raw Data| DP[Data Preprocessing]
        DP -->|Encoded Features| RiskModel[Risk Model]
        DP -->|Encoded Features| SGPAModel[SGPA Model]
        RiskModel -->|Probabilities| RS[Risk Scoring Logic]
        SGPAModel -->|SGPA Band| PL[Projection Logic]
    end
    RS -->|Risk Level| API
    PL -->|Projected SGPA/CGPA| API
    API -->|JSON Response| FE
    FE -->|Visual Alert| User
    
    style User fill:#f9f,stroke:#333,stroke-width:2px
    style Model fill:#bbf,stroke:#333,stroke-width:2px
    style RS fill:#dfd,stroke:#333,stroke-width:2px
```

---

## 🛠️ Tech Stack

*   **Core**: Python 3.9
*   **ML Framework**: Scikit-Learn (Random Forest, Logistic Regression)
*   **Data Structure**: Pandas, NumPy
*   **Web Framework**: Flask (Jinja2 Templates)
*   **Frontend**: HTML5, CSS3 (Custom Responsive Design)
*   **Packaging**: PyInstaller

---

## 📂 Project Structure

```bash
AI Grade Prediction/
├── 📁 app/          # Flask application logic
│   ├── 📁 templates/ # HTML frontend
│   └── 📁 static/    # CSS assets
├── 📁 assets/       # Project banner and media
├── 📁 data/         # Student performance datasets
├── 📁 models/       # Pkl files for Models & Encoders
├── 📁 src/          # ML scripts (Training, Evaluation)
├── 📁 dist/         # Standalone Executable (.exe)
└── 📄 HOW_TO_RUN.txt # Comprehensive usage guide
```

---

## 🚀 Quick Start

### 👨‍💻 For Users (No Coding Needed)
1.  Go to the `dist/` folder.
2.  Double-click **`student_risk_predictor.exe`**.
3.  The application will launch in your browser automatically at `http://127.0.0.1:5000`.

### ⚙️ For Developers
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/MrRenntech/AI-Grade-Prediction.git
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application**:
    ```bash
    python app/app.py
    ```

---

## 🤖 Model Performance

We evaluated multiple models to ensure the highest reliability:

| Model | Accuracy | Precision | Recall | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **Random Forest** | **91.1%** | **0.90** | **0.92** | **Selected 🏆** |
| Logistic Regression | 84.8% | 0.83 | 0.85 | Baseline |

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

*Built with ❤️ for Educational Technology.*
