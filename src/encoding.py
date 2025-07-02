import pandas as pd


def encode_features(df):
    df = df.copy()

    # Label Encoding
    binary_cols = ['gender','Partner','Dependents','PhoneService','PaperlessBilling']
    for col in binary_cols:
        df[col] = df[col].map({'Yes': 1,'No': 0, 'Female': 1,'Male':0})

    # One-Hot Encoding
    other_cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    other_cat_cols = [col for col in other_cat_cols if col not in binary_cols + ["Churn"]]

    df= pd.get_dummies(df,columns=other_cat_cols,drop_first=True)

    return df
