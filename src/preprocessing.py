import pandas as pd
import os

def clean_data(df):
    df = df.copy()

    # Remove customerID
    if "customerID" in df.columns:
        df.drop(["customerID"],axis=1,inplace=True)

    # TotalCharges -> numeric, incorrect values become NaN
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"],errors="coerce")

    # Remove NaN rows
    df=df.dropna(subset=["TotalCharges"])

    # Churn: Yes -> 1, No -> 0
    df["Churn"] = df["Churn"].map({"Yes": 1,"No": 0})
    return df

def save_clean_data(df,output_path="data/processed/clean_telco.csv"):
    os.makedirs(os.path.dirname(output_path),exist_ok=True)
    df.to_csv(output_path,index=False)
    print(f"Clean data saved successfully: {output_path}")