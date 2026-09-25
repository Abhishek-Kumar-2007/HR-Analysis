import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Locate project folder
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = PROJECT_DIR / "data" / "HR_Analytics_Python_Cleaned.xlsx"


# --------------------------------------------------
# 2. Load data
# --------------------------------------------------

df = pd.read_excel(DATA_FILE)


# --------------------------------------------------
# 3. Dataset information
# --------------------------------------------------

print("\n========== DATASET INFORMATION ==========\n")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nData Types:")
print(df.dtypes)


# --------------------------------------------------
# 4. Missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========\n")

print(df.isnull().sum())


# --------------------------------------------------
# 5. Statistical summary
# --------------------------------------------------

print("\n========== STATISTICAL SUMMARY ==========\n")

print(df.describe())


# --------------------------------------------------
# 6. Employee Status
# --------------------------------------------------

print("\n========== EMPLOYEE STATUS ==========\n")

print(df["employee_status"].value_counts())


# --------------------------------------------------
# 7. Department
# --------------------------------------------------

print("\n========== DEPARTMENT ==========\n")

print(df["department_type"].value_counts())


# --------------------------------------------------
# 8. Performance
# --------------------------------------------------

print("\n========== PERFORMANCE ==========\n")

print(df["performance_score"].value_counts())


# --------------------------------------------------
# 9. Training Outcome
# --------------------------------------------------

print("\n========== TRAINING OUTCOME ==========\n")

print(df["training_outcome"].value_counts())


# --------------------------------------------------
# 10. Training Type
# --------------------------------------------------

print("\n========== TRAINING TYPE ==========\n")

print(df["training_type"].value_counts())