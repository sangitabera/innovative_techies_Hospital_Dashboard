import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

MODEL_PATH = "models/risk_model.pkl"
SCALER_PATH = "models/scaler.pkl"


def preprocess(df):
    # Convert HEX → int safely
    df["heart_rate"] = df["heart_rate_hex"].apply(
        lambda x: int(x, 16) if pd.notnull(x) else None
    )

    # Select features
    features = df[["heart_rate", "spO2", "age"]].copy()

    # 🔥 HANDLE MISSING VALUES
    features["heart_rate"].fillna(features["heart_rate"].median(), inplace=True)
    features["spO2"].fillna(features["spO2"].median(), inplace=True)
    features["age"].fillna(features["age"].median(), inplace=True)

    return features


def generate_labels(df):
    """
    Since no labels are given, we simulate:
    High risk if:
    - heart_rate > 120 OR
    - spO2 < 90 OR
    - age > 65
    """
    labels = (
        (df["heart_rate"] > 120) |
        (df["spO2"] < 90) |
        (df["age"] > 65)
    ).astype(int)

    return labels



def train_model(df):
    X = preprocess(df)
    y = generate_labels(df)

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("model", LogisticRegression())
    ])

    pipeline.fit(X, y)

    joblib.dump(pipeline, MODEL_PATH)

    print("✅ Model trained with NaN handling!")


def load_model():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    return model, scaler


def predict_risk(df):
    model = joblib.load(MODEL_PATH)

    X = preprocess(df)

    probs = model.predict_proba(X)[:, 1]

    df["risk_score"] = probs

    return df