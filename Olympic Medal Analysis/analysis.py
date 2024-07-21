# analysis.py
import file_handling
from exception import DataCleaningError
import data_cleaning  

def main():
    df = file_handling.read_csv('olympic_medals.csv')
    try:
        df = data_cleaning.clean_data(df)
        file_handling.write_csv('clean_olympic_medals.csv', df)
    except DataCleaningError as e:
        print(f"Data cleaning error: {e.message}")
        return

main()

