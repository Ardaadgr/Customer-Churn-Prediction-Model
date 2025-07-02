from src.data_loader import load_data
from src.preprocessing import clean_data, save_clean_data
from src.encoding import encode_features


df = load_data()


if df is not None:
    print(df.head())
    print(df.info())
    print(df.isnull().sum())
    print(df[df["TotalCharges"].str.strip() == " "])

df_clean = clean_data(df)

print(df_clean.head())

save_clean_data(df_clean)
categorical_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
print(categorical_cols)

df_encoded = encode_features(df_clean)
print(df_encoded.head())