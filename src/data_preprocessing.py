import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(path, return_encoders=False):
    """
    Loads the student dataset, preprocesses features, and encodes target variable.
    
    Args:
        path (str): Path to the CSV file.
        return_encoders (bool): If True, returns the trained LabelEncoders (for inference).
        
    Returns:
        X (pd.DataFrame): Feature matrix.
        y (pd.Series): Target vector (Risk).
        encoders (dict): Dictionary of {column_name: LabelEncoder_object} (optional).
    """
    # Load dataset
    df = pd.read_csv(path, sep=',')

    # Define Risk Labeling Logic
    # G3 is the final grade (0-20). 
    # < 10: Fail (High Risk)
    # 10-13: Borderline/Average (Medium Risk) - simplified to 1 here if needed, or keeping logic consistent
    # But wait, looking at original logic:
    # < 10 -> 2 (High Risk)
    # < 14 -> 1 (Medium Risk)
    # >= 14 -> 0 (Low Risk)
    def risk_label(g3):
        if g3 < 10:
            return 2  # High Risk
        elif g3 < 14:
            return 1  # Medium Risk
        else:
            return 0  # Low Risk

    # Create target column
    df['risk'] = df['G3'].apply(risk_label)

    # Drop the target leakage column (G3 is what we want to predict indirectly via risk)
    df.drop(columns=['G3'], inplace=True)

    encoders = {}
    # Identify categorical columns and encode them
    # We use LabelEncoder to convert strings ('yes', 'no', 'F', 'M') into integers (1, 0, etc.)
    for col in df.select_dtypes(include='object').columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le  # Store encoder to handle new data later

    # Separate Features (X) and Target (y)
    X = df.drop('risk', axis=1)
    y = df['risk']

    if return_encoders:
        return X, y, encoders
    
    return X, y
