import pandas as pd
from csvToDF import csv_to_df 
df : pd.DataFrame = csv_to_df(r"dummy_data\student_score.csv")

def avg_score(df: pd.DataFrame) -> float:
    avg = df["Score"].mean()
    return avg

# print("Avg Score of students is",avg_score(student_rank))

df["Grade"] = df["Score"].apply(lambda x: "A" if x < 95 else 'B' if x < 85 else 'C' if x < 75 else 'E')




df["Status"] = df["Grade"].apply(lambda x: "Fail" if x == 'E' else 'Pass')

print(df)