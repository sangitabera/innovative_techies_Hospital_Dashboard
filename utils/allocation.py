def allocate_ward(df, icu_capacity=10, general_capacity=20):
    df = df.sort_values(by="risk_score", ascending=False)

    df["ward"] = "Waiting"

    icu_patients = df.head(icu_capacity).index
    general_patients = df.iloc[icu_capacity:icu_capacity+general_capacity].index

    df.loc[icu_patients, "ward"] = "ICU"
    df.loc[general_patients, "ward"] = "General"

    return df