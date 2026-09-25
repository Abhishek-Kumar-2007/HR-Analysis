import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Locate the project folder
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = PROJECT_DIR / "data" / "HR_Analytics_Cleaned.xlsx"


# --------------------------------------------------
# 2. Load the Excel dataset
# --------------------------------------------------

df = pd.read_excel(DATA_FILE)


# --------------------------------------------------
# 3. Basic information
# --------------------------------------------------

print("\n========== DATASET LOADED SUCCESSFULLY ==========\n")

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())


# --------------------------------------------------
# 4. Display first 5 rows
# --------------------------------------------------

print("\n========== FIRST 5 ROWS ==========\n")

print(df.head())


# --------------------------------------------------
# 5. Display data types
# --------------------------------------------------

print("\n========== DATA TYPES ==========\n")

print(df.dtypes)