import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_sgpa_data(path):
    df = pd.read_csv(path, sep=',')

    # SGPA band mapping from final grade
    def sgpa_band(g3):
        if g3 < 10:
            return 0
        elif g3 < 12:
            return 1
        elif g3 < 14:
            return 2
        elif g3 < 16:
            return 3
        else:
            return 4

    df["sgpa_band"] = df["G3"].apply(sgpa_band)

    # Use only features available before final exam
    df["G1_G2_AVG"] = (df["G1"] + df["G2"]) / 2
    df.drop(columns=["G1", "G2", "G3"], inplace=True)

    # Encode categoricals
    for col in df.select_dtypes(include="object").columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    X = df.drop("sgpa_band", axis=1)
    y = df["sgpa_band"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler
