from src.data_loader import load_data

df = load_data()

if df is not None:
    print(df.head())
    print(df.info())
    print(df.isnull().sum())