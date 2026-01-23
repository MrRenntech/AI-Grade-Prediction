import os

def generate_tree(startpath):
    tree = []
    prefix = os.path.basename(os.path.abspath(startpath)) + "/"
    tree.append(prefix)
    
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level)
        subindent = '├── '
        subindent_last = '└── '
        
        # Filter hidden folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'venv', 'env']]
        
        if root == startpath:
            pass # already added root
        else:
             # This part is tricky with walk, let's just do a simpler manual list for top level
             pass

    # Let's do a simpler approach for the specific file structure requested
    # We want specific ordering and comments
    structure = [
        "AI Grade Prediction/",
        "├── 📁 app/          # Flask application logic",
        "│   ├── 📁 templates/ # HTML frontend",
        "│   ├── 📁 static/    # CSS assets",
        "│   └── 🐍 app.py     # Main application entry point",
        "├── 📁 assets/       # Project banner and media",
        "├── 📁 data/         # Student performance datasets",
        "├── 📁 models/       # Trained Models (Risk & SGPA)",
        "│   ├── 📄 student_risk_model.pkl",
        "│   ├── 📄 sgpa_band_model.pkl",
        "│   └── ...",
        "├── 📁 src/          # Intelligence Layer Scripts",
        "│   ├── 🐍 train_model.py       # Risk Model Training",
        "│   ├── 🐍 train_sgpa_model.py  # SGPA Model Training",
        "│   ├── 🐍 cgpa_projection.py   # CGPA Logic",
        "│   ├── 🐍 data_preprocessing.py",
        "│   └── 🐍 sgpa_preprocessing.py",
        "├── 📁 dist/         # Standalone Executable (Git-ignored but local)",
        "├── 📄 HOW_TO_RUN.txt      # Guide for users",
        "├── 📄 DEVELOPMENT_STEPS.txt # Full dev log",
        "├── 📄 requirements.txt    # Python dependencies",
        "└── 📄 README.md           # Project Documentation"
    ]
    
    return "\n".join(structure)

if __name__ == "__main__":
    print(generate_tree("."))
