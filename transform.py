import numpy as np

def transform_data(df):
    print("Transforming data...")

    # Convert negative days to age
    df["age"] = (df["DAYS_BIRTH"] / -365).astype(int)

    # Handle missing income
    df["AMT_INCOME_TOTAL"].fillna(df["AMT_INCOME_TOTAL"].median(), inplace=True)

    # Remove extreme income outliers
    df = df[df["AMT_INCOME_TOTAL"] < df["AMT_INCOME_TOTAL"].quantile(0.99)]

    # Create derived features
    df["loan_to_income"] = df["AMT_CREDIT"] / df["AMT_INCOME_TOTAL"]
    df["emi_burden"] = df["AMT_ANNUITY"] / df["AMT_INCOME_TOTAL"]

    return df
