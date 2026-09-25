import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Locate project folder
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = PROJECT_DIR / "data" / "HR_Analytics_Cleaned.xlsx"

OUTPUT_FILE = PROJECT_DIR / "data" / "HR_Analytics_Python_Cleaned.xlsx"


# --------------------------------------------------
# 2. Load dataset
# --------------------------------------------------

df = pd.read_excel(INPUT_FILE)

print("\n========== ORIGINAL DATA ==========\n")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# --------------------------------------------------
# 3. Remove completely empty rows and columns
# --------------------------------------------------

df = df.dropna(axis=0, how="all")
df = df.dropna(axis=1, how="all")


# --------------------------------------------------
# 4. Remove duplicate rows
# --------------------------------------------------

duplicates = df.duplicated().sum()

print("\nDuplicate rows found:", duplicates)

df = df.drop_duplicates()


# --------------------------------------------------
# 5. Remove duplicate Employee IDs
# --------------------------------------------------

duplicate_employee_ids = df["employee_id"].duplicated().sum()

print("Duplicate Employee IDs:", duplicate_employee_ids)


# --------------------------------------------------
# 6. Convert date columns
# --------------------------------------------------

date_columns = [
    "start_date",
    "dob",
    "survey_date",
    "training_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(
        df[column],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    )


# --------------------------------------------------
# 7. Check missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========\n")

print(df.isnull().sum())


# --------------------------------------------------
# 8. Save cleaned dataset
# --------------------------------------------------

df.to_excel(
    OUTPUT_FILE,
    index=False
)

print("\n========== CLEANING COMPLETE ==========\n")

print("Final Rows:", len(df))
print("Final Columns:", len(df.columns))

print("\nSaved file:")
print(OUTPUT_FILE)