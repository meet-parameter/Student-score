import pandas as pd
import os

def csvTodf(file_path: str):
    if not os.path.exists(file_path):
        return FileNotFoundError
    