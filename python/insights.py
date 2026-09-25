import pandas as pd
from pathlib import Path

# ==========================================
# 1. LOAD DATA
# ==========================================

BASE_DIR = Path(__file__).resolve().parents[1]

file_path = BASE_DIR / "data" / "HR_Analytics_Python_Cleaned.xlsx"

df = pd.read_excel(file_path)

print("=" * 60)
print("HR ANALYTICS - FINAL INSIGHTS")
print("=" * 60)


# ==========================================
# 2. BASIC WORKFORCE SUMMARY
# ==========================================

total_employees = len(df)

active_employees = (df["employee_status"] == "Active").sum()
terminated_employees = (df["employee_status"] == "Terminated").sum()

active_percentage = active_employees / total_employees * 100
terminated_percentage = terminated_employees / total_employees * 100

print("\n--- WORKFORCE SUMMARY ---")

print("Total Employees:", total_employees)
print("Active Employees:", active_employees)
print("Terminated Employees:", terminated_employees)

print(f"Active Share: {active_percentage:.2f}%")
print(f"Terminated Share: {terminated_percentage:.2f}%")


# ==========================================
# 3. EMPLOYEE EXPERIENCE
# ==========================================

print("\n--- EMPLOYEE EXPERIENCE ---")

avg_engagement = df["engagement_score"].mean()
avg_satisfaction = df["satisfaction_score"].mean()
avg_worklife = df["work_life_balance_score"].mean()
avg_rating = df["current_employee_rating"].mean()

print(f"Average Engagement Score: {avg_engagement:.2f}")
print(f"Average Satisfaction Score: {avg_satisfaction:.2f}")
print(f"Average Work-Life Balance Score: {avg_worklife:.2f}")
print(f"Average Employee Rating: {avg_rating:.2f}")


# ==========================================
# 4. DEPARTMENT ANALYSIS
# ==========================================

print("\n--- DEPARTMENT ANALYSIS ---")

department_counts = df["department_type"].value_counts()

largest_department = department_counts.idxmax()

print("Largest Department:", largest_department)
print("Employees in Largest Department:", department_counts.max())

print("\nDepartment-wise Employee Count:")
print(department_counts)


# ==========================================
# 5. DEPARTMENT TERMINATION ANALYSIS
# ==========================================

print("\n--- DEPARTMENT TERMINATION ANALYSIS ---")

department_status = pd.crosstab(
    df["department_type"],
    df["employee_status"]
)

department_status["Total"] = department_status.sum(axis=1)

if "Terminated" in department_status.columns:
    department_status["Termination %"] = (
        department_status["Terminated"]
        / department_status["Total"]
        * 100
    )

print(department_status.round(2))


# ==========================================
# 6. DEPARTMENT ENGAGEMENT
# ==========================================

print("\n--- DEPARTMENT ENGAGEMENT ---")

department_engagement = (
    df.groupby("department_type")["engagement_score"]
    .mean()
    .sort_values(ascending=False)
)

print(department_engagement.round(2))

highest_engagement_department = department_engagement.idxmax()
lowest_engagement_department = department_engagement.idxmin()

print("\nHighest Average Engagement:")
print(highest_engagement_department)

print("\nLowest Average Engagement:")
print(lowest_engagement_department)


# ==========================================
# 7. PERFORMANCE ANALYSIS
# ==========================================

print("\n--- PERFORMANCE ANALYSIS ---")

performance_counts = df["performance_score"].value_counts()

print(performance_counts)

print("\nPerformance Percentages:")

performance_percentage = (
    df["performance_score"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print(performance_percentage)


# ==========================================
# 8. PERFORMANCE VS TERMINATION
# ==========================================

print("\n--- PERFORMANCE VS EMPLOYEE STATUS ---")

performance_status = pd.crosstab(
    df["performance_score"],
    df["employee_status"]
)

performance_status["Total"] = performance_status.sum(axis=1)

if "Terminated" in performance_status.columns:
    performance_status["Termination %"] = (
        performance_status["Terminated"]
        / performance_status["Total"]
        * 100
    )

print(performance_status.round(2))


# ==========================================
# 9. TRAINING ANALYSIS
# ==========================================

print("\n--- TRAINING ANALYSIS ---")

total_training_cost = df["training_cost_in_Rupees"].sum()
average_training_cost = df["training_cost_in_Rupees"].mean()

average_training_duration = df["training_duration_days"].mean()

print(f"Total Training Cost: Rs. {total_training_cost:,.2f}")
print(f"Average Training Cost: Rs. {average_training_cost:,.2f}")
print(f"Average Training Duration: {average_training_duration:.2f} days")


# ==========================================
# 10. TRAINING PROGRAM ANALYSIS
# ==========================================

print("\n--- TRAINING PROGRAM ANALYSIS ---")

training_program = (
    df.groupby("training_program_name")
    .agg(
        Participants=("training_program_name", "count"),
        Total_Cost=("training_cost_in_Rupees", "sum"),
        Average_Duration=("training_duration_days", "mean")
    )
)

training_program["Cost_Per_Participant"] = (
    training_program["Total_Cost"]
    / training_program["Participants"]
)

print(training_program.round(2))


# ==========================================
# 11. TRAINING COST INSIGHTS
# ==========================================

print("\n--- TRAINING COST INSIGHTS ---")

highest_training_cost_program = (
    training_program["Total_Cost"].idxmax()
)

highest_cost_per_participant_program = (
    training_program["Cost_Per_Participant"].idxmax()
)

print("Highest Total Training Cost Program:")
print(highest_training_cost_program)

print("\nHighest Cost per Participant Program:")
print(highest_cost_per_participant_program)


# ==========================================
# 12. TRAINING OUTCOME ANALYSIS
# ==========================================

print("\n--- TRAINING OUTCOME ANALYSIS ---")

training_outcomes = df["training_outcome"].value_counts()

print(training_outcomes)

training_outcome_percentage = (
    df["training_outcome"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nTraining Outcome Percentages:")
print(training_outcome_percentage)


# ==========================================
# 13. TRAINING TYPE ANALYSIS
# ==========================================

print("\n--- TRAINING TYPE ANALYSIS ---")

training_type = df["training_type"].value_counts()

print(training_type)

training_type_percentage = (
    df["training_type"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nTraining Type Percentages:")
print(training_type_percentage)


# ==========================================
# 14. CORRELATION ANALYSIS
# ==========================================

print("\n--- CORRELATION ANALYSIS ---")

correlation_columns = [
    "engagement_score",
    "satisfaction_score",
    "work_life_balance_score",
    "current_employee_rating",
    "training_duration_days",
    "training_cost_in_Rupees",
    "age"
]

correlation_matrix = df[correlation_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))

engagement_satisfaction_correlation = (
    correlation_matrix.loc[
        "engagement_score",
        "satisfaction_score"
    ]
)

print(
    f"\nEngagement vs Satisfaction Correlation: "
    f"{engagement_satisfaction_correlation:.2f}"
)


# ==========================================
# 15. SAVE IMPORTANT ANALYSIS FILES
# ==========================================

output_dir = BASE_DIR / "outputs"
output_dir.mkdir(exist_ok=True)

department_status.to_csv(
    output_dir / "department_termination_analysis.csv"
)

performance_status.to_csv(
    output_dir / "performance_termination_analysis.csv"
)

training_program.to_csv(
    output_dir / "training_program_analysis.csv"
)

correlation_matrix.to_csv(
    output_dir / "correlation_matrix.csv"
)


# ==========================================
# 16. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("FINAL PROJECT SUMMARY")
print("=" * 60)

print(f"""
Total Employees              : {total_employees}
Active Employees             : {active_employees}
Terminated Employees         : {terminated_employees}

Average Engagement           : {avg_engagement:.2f}
Average Satisfaction         : {avg_satisfaction:.2f}
Average Work-Life Balance    : {avg_worklife:.2f}
Average Employee Rating      : {avg_rating:.2f}

Largest Department           : {largest_department}
Highest Engagement Dept.     : {highest_engagement_department}
Lowest Engagement Dept.      : {lowest_engagement_department}

Total Training Cost          : Rs. {total_training_cost:,.2f}
Average Training Cost        : Rs. {average_training_cost:,.2f}
Average Training Duration    : {average_training_duration:.2f} days

Highest Training Cost        : {highest_training_cost_program}
Highest Cost/Participant     : {highest_cost_per_participant_program}

Engagement-Satisfaction Corr.: {engagement_satisfaction_correlation:.2f}
""")

print("=" * 60)
print("Analysis completed successfully!")
print("=" * 60)