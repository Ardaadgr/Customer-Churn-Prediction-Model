from src.data_loader import load_data
from src.preprocessing import clean_data, save_clean_data


df = load_data()


if df is not None:
    print(df.head())
    print(df.info())
    print(df.isnull().sum())
    print(df[df["TotalCharges"].str.strip() == " "])

df_clean = clean_data(df)

print(df_clean.head())

save_clean_data(df_clean)