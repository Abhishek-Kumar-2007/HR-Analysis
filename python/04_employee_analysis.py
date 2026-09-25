import pandas as pd
from pathlib import Path


# --------------------------------------------------
# 1. Locate project folder
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = PROJECT_DIR / "data" / "HR_Analytics_Python_Cleaned.xlsx"

OUTPUT_DIR = PROJECT_DIR / "outputs"

OUTPUT_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 2. Load data
# --------------------------------------------------

df = pd.read_excel(DATA_FILE)


# --------------------------------------------------
# 3. Employee Status Analysis
# --------------------------------------------------

print("\n========== EMPLOYEE STATUS ==========\n")

status_count = df["employee_status"].value_counts()

print(status_count)

status_percentage = (
    df["employee_status"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nPercentage:")
print(status_percentage)


# --------------------------------------------------
# 4. Department Analysis
# --------------------------------------------------

print("\n========== DEPARTMENT ANALYSIS ==========\n")

department_count = (
    df["department_type"]
    .value_counts()
)

print(department_count)


# --------------------------------------------------
# 5. Performance Analysis
# --------------------------------------------------

print("\n========== PERFORMANCE ANALYSIS ==========\n")

performance_count = (
    df["performance_score"]
    .value_counts()
)

print(performance_count)


# --------------------------------------------------
# 6. Average HR Scores
# --------------------------------------------------

print("\n========== AVERAGE HR SCORES ==========\n")

print(
    "Average Engagement:",
    round(df["engagement_score"].mean(), 2)
)

print(
    "Average Satisfaction:",
    round(df["satisfaction_score"].mean(), 2)
)

print(
    "Average Work-Life Balance:",
    round(df["work_life_balance_score"].mean(), 2)
)

print(
    "Average Employee Rating:",
    round(df["current_employee_rating"].mean(), 2)
)


# --------------------------------------------------
# 7. Department-wise Engagement
# --------------------------------------------------

print("\n========== DEPARTMENT-WISE ENGAGEMENT ==========\n")

department_engagement = (
    df.groupby("department_type")["engagement_score"]
    .mean()
    .sort_values(ascending=False)
)

print(department_engagement)


# --------------------------------------------------
# 8. Department vs Employee Status
# --------------------------------------------------

print("\n========== DEPARTMENT VS EMPLOYEE STATUS ==========\n")

department_status = pd.crosstab(
    df["department_type"],
    df["employee_status"]
)

print(department_status)


# --------------------------------------------------
# 9. Performance vs Employee Status
# --------------------------------------------------

print("\n========== PERFORMANCE VS EMPLOYEE STATUS ==========\n")

performance_status = pd.crosstab(
    df["performance_score"],
    df["employee_status"]
)

print(performance_status)


# --------------------------------------------------
# 10. Save analysis tables
# --------------------------------------------------

department_engagement.to_csv(
    OUTPUT_DIR / "department_engagement.csv"
)

department_status.to_csv(
    OUTPUT_DIR / "department_status.csv"
)

performance_status.to_csv(
    OUTPUT_DIR / "performance_status.csv"
)

print("\nAnalysis tables saved successfully.")