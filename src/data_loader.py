import pandas as pd
import os

from pandas.io.common import file_path_to_url


def load_data(filename="telco_churn.csv",data_dir="data/raw/"):
    filepath = os.path.join(data_dir,filename)
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully: {df.shape[0]} row, {df.shape[1]} column")
        return df
    except FileNotFoundError:
        print(f"Data Not Found!: {filepath}")
        return None
