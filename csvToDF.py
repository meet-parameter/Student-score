import pandas as pd
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def csv_to_df(file_path: str):
    try:
        df = pd.read_csv(file_path)
        logger.info(f"the file {file_path} Found successfully!!!")
        return df
    except FileNotFoundError:
        return logger.error(f"The file at path {file_path} does not exist")

