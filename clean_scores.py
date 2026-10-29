
import pandas as pd
import os
import logging
from csvToDF import csv_to_df

logger = logging.info(__name__)



def fill_missing_score(file_path):
    try:
        print("Current working directory:", os.getcwd())
        
        df = csv_to_df(file_path)

        if df is None:
            return

        print("Columns:", df.columns)

        # Check if Score column exists
        if "Score" not in df.columns:
            logging.error("Score column not found")
            print("Score column not found")
            return

        # Fill missing scores with the mean
        df["Score"] = df["Score"].fillna(df["Score"].mean())

        # Save the updated CSV file
        df.to_csv(file_path, index=False)

        print("Updated DataFrame:")
        print(df)

        logger.info("Missing scores filled successfully in csv file")

    except FileNotFoundError:
        logger.error("CSV file not found")
        print("File not found. Please check the file path.")

    except Exception as e:
        logger.error(f"Something went wrong: {e}")
        print("An error occurred:", e)


file_path = r"C:\Users\admin\Documents\Python Advance\VE\Student-score\dummy_data\student_score.csv"

cleaned_df = fill_missing_score(file_path)

print(cleaned_df)
