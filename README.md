<div align="center">

# 🎓 AI Grade Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green?style=for-the-badge&logo=flask&logoColor=white)
![Sklearn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

**An intelligent, data-driven system to predict student academic risk using ML.**
</div>

---

## 🏗️ System Architecture

```mermaid
graph LR
    User[Educator Input] --> API[Flask API]
    API --> RF[Decision Model - RF 91%]
    RF --> Risk[Risk Score]
    RF --> Proj[CGPA Projection]
    Risk & Proj --> API --> UI[Dashboard]
```

## 🚀 Quick Start
Run standalone `.exe` distributable or `python app/app.py`.
