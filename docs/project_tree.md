# 🌳 Project Directory Structure

```plaintext
AI Grade Prediction/
├── 📁 app/                    # Flask application logic
│   ├── 📁 templates/          # HTML frontend for the web app
│   ├── 📁 static/             # CSS and JS assets
│   └── 🐍 app.py              # Main application entry point
├── 📁 assets/                 # Project banner and media resources
├── 📁 data/                   # Student performance datasets
├── 📁 models/                 # Trained Models (Risk & SGPA)
│   ├── 📄 student_risk_model.pkl
│   ├── 📄 sgpa_band_model.pkl
│   └── 📄 sgpa_scaler.pkl
├── 📁 src/                    # Intelligence Layer Scripts & Helpers
│   ├── 🐍 train_model.py      # Risk Model Training Script
│   ├── 🐍 train_sgpa_model.py # SGPA Model Training Script
│   ├── 🐍 cgpa_projection.py  # Logic for CGPA Projection
│   ├── 🐍 data_preprocessing.py # Data Cleaning Pipeline
│   └── 🐍 sgpa_preprocessing.py # SGPA-specific Preprocessing
├── 📁 dist/                   # Standalone Executables
├── 📁 docs/                   # 📚 Project Documentation (You are here!)
├── 📄 requirements.txt        # Python dependency list
└── 📄 README.md               # Main Project Documentation
```
