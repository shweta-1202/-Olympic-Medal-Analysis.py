import pandas as pd

def read_csv(file_name):
    return pd.read_csv(file_name)

def write_csv(file_name, df):
    df.to_csv(file_name, index=False)