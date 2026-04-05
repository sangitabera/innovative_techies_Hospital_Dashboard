import numpy as np

def simulate_vitals(df):
    df["heart_rate"] = df["heart_rate"] + np.random.randint(-5, 5, size=len(df))
    df["spO2"] = df["spO2"] + np.random.randint(-2, 2, size=len(df))

    df["heart_rate"] = df["heart_rate"].clip(40, 180)
    df["spO2"] = df["spO2"].clip(70, 100)

    return df