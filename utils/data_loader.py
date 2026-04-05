import pandas as pd

def load_data():
    patients = pd.read_csv("data\patient_demographics.csv")
    telemetry = pd.read_csv('data\Telemetry_logs.csv')
    prescriptions = pd.read_csv("data\prescription_audit.csv")

    return patients, telemetry, prescriptions


def merge_data(patients, telemetry, prescriptions):
    df = telemetry.merge(patients, on="ghost_id", how="left")
    df = df.merge(prescriptions, on="ghost_id", how="left")
    return df