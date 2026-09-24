import pandas as pd
import numpy as np
df = pd.read_excel("HR_Analytics_Cleaned.xlsx")
print(df.head())

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print(df.columns.tolist())

print(df.dtypes)
date_columns = [
    "start_date",
    "dob",
    "survey_date",
    "training_date"
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors="coerce")
    print(df[date_columns].dtypes)
    missing_values = df.isnull().sum()

print(missing_values)

missing_report = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum().values,
    "Missing %": (df.isnull().sum().values / len(df) * 100).round(2)
})

print(missing_report)

print("Duplicate rows:", df.duplicated().sum())

print("Duplicate Employee IDs:", df["employee_id"].duplicated().sum())
#Statistical summary
print(df.describe())
#employee status
print(df["employee_status"].value_counts())
#Department
print(df["department_type"].value_counts())
#Job title
print(df["title"].value_counts())
#Gender
print(df["gender_code"].value_counts())
#Training outcome
print(df["training_outcome"].value_counts())
#Training type
print(df["training_type"].value_counts())

#Calculate the number of employees in each status:
status_counts = df["employee_status"].value_counts()

print(status_counts)

#Now calculate percentages:
status_percentage = (
    df["employee_status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print(status_percentage)
