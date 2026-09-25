import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


# --------------------------------------------------
# 1. Locate project folder
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = PROJECT_DIR / "data" / "HR_Analytics_Python_Cleaned.xlsx"

VISUAL_DIR = PROJECT_DIR / "visualizations"

VISUAL_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# 2. Load data
# --------------------------------------------------

df = pd.read_excel(DATA_FILE)


# --------------------------------------------------
# 3. Employee Status
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="employee_status"
)

plt.title("Employee Status Distribution")
plt.xlabel("Employee Status")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "employee_status.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 4. Department Distribution
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    y="department_type",
    order=df["department_type"].value_counts().index
)

plt.title("Employees by Department")
plt.xlabel("Number of Employees")
plt.ylabel("Department")

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "department_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 5. Performance Distribution
# --------------------------------------------------

plt.figure(figsize=(9, 5))

sns.countplot(
    data=df,
    x="performance_score",
    order=df["performance_score"].value_counts().index
)

plt.title("Employee Performance Distribution")
plt.xlabel("Performance Score")
plt.ylabel("Number of Employees")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "performance_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 6. Engagement Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="engagement_score"
)

plt.title("Employee Engagement Score")
plt.xlabel("Engagement Score")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "engagement_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 7. Satisfaction Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="satisfaction_score"
)

plt.title("Employee Satisfaction Score")
plt.xlabel("Satisfaction Score")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "satisfaction_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 8. Satisfaction vs Engagement
# --------------------------------------------------

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="satisfaction_score",
    y="engagement_score"
)

plt.title("Employee Satisfaction vs Engagement")
plt.xlabel("Satisfaction Score")
plt.ylabel("Engagement Score")

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "satisfaction_vs_engagement.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 9. Correlation Heatmap
# --------------------------------------------------

numeric_columns = [
    "engagement_score",
    "satisfaction_score",
    "work_life_balance_score",
    "current_employee_rating",
    "training_duration_days",
    "training_cost_in_Rupees",
    "age"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("HR Metrics Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 10. Training Programs
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    y="training_program_name",
    order=df["training_program_name"].value_counts().index
)

plt.title("Employees by Training Program")
plt.xlabel("Number of Employees")
plt.ylabel("Training Program")

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "training_programs.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 11. Training Outcome
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="training_outcome"
)

plt.title("Training Outcome Distribution")
plt.xlabel("Training Outcome")
plt.ylabel("Number of Employees")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "training_outcome.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 12. Training Cost by Program
# --------------------------------------------------

training_cost = (
    df.groupby("training_program_name")[
        "training_cost_in_Rupees"
    ]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

training_cost.plot(kind="bar")

plt.title("Total Training Cost by Program")
plt.xlabel("Training Program")
plt.ylabel("Total Training Cost")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "training_cost_by_program.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 13. Age Distribution
# --------------------------------------------------

plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x="age",
    bins=20,
    kde=True
)

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Employees")

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "age_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 14. Department vs Employee Status
# --------------------------------------------------

department_status = pd.crosstab(
    df["department_type"],
    df["employee_status"]
)

department_status.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Employee Status by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "department_vs_status.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


# --------------------------------------------------
# 15. Department vs Engagement
# --------------------------------------------------

department_engagement = (
    df.groupby("department_type")["engagement_score"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

department_engagement.plot(kind="bar")

plt.title("Average Employee Engagement by Department")
plt.xlabel("Department")
plt.ylabel("Average Engagement Score")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    VISUAL_DIR / "department_engagement.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()


print("\n========== ALL VISUALIZATIONS CREATED ==========\n")

print("Saved in:")
print(VISUAL_DIR)