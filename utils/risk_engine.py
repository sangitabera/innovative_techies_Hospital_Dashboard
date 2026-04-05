import numpy as np

def compute_risk_score(df):
    # Convert hex heart rate
    df["heart_rate"] = df["heart_rate_hex"].apply(lambda x: int(x, 16))

    # Normalize features
    hr_score = df["heart_rate"] / 200
    spo2_score = (100 - df["spO2"]) / 100
    age_score = df["age"] / 100

    # Final risk score
    df["risk_score"] = (0.5 * hr_score + 0.3 * spo2_score + 0.2 * age_score)

    return df