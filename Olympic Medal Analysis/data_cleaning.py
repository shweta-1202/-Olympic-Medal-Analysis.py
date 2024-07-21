# datacleaning.py
import pandas as pd
from exception import DataCleaningError

def load_data(file_name):
    try:
        df = pd.read_csv(file_name)
        return df
    except pd.errors.EmptyDataError:
        raise DataCleaningError("Data is empty")
    except pd.errors.ParserError:
        raise DataCleaningError("Data is not in CSV format")
    except FileNotFoundError:
        raise DataCleaningError("File not found")

def clean_data(df):
    print("Missing Values per Column")
    print(df.isnull().sum())
    print("Number of Duplicate Rows")
    print(df.duplicated().sum())
    
    df = df.fillna(0)
    df = df.drop_duplicates()

    # Rechecking the null values 
    
    print(df.isnull().sum())
    print(df.duplicated().sum())

    # Drop specified columns
    # columns_to_remove = ['country_code', 'country_3_letter_code', 'athlete_url']
    # df = df.drop(columns=columns_to_remove)
    
    return df
