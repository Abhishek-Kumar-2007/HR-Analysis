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
# 3. Training Program Analysis
# --------------------------------------------------

print("\n========== TRAINING PROGRAMS ==========\n")

training_programs = (
    df["training_program_name"]
    .value_counts()
)

print(training_programs)


# --------------------------------------------------
# 4. Training Outcome
# --------------------------------------------------

print("\n========== TRAINING OUTCOME ==========\n")

training_outcome = (
    df["training_outcome"]
    .value_counts()
)

print(training_outcome)


# --------------------------------------------------
# 5. Training Type
# --------------------------------------------------

print("\n========== TRAINING TYPE ==========\n")

training_type = (
    df["training_type"]
    .value_counts()
)

print(training_type)


# --------------------------------------------------
# 6. Training Cost
# --------------------------------------------------

print("\n========== TRAINING COST ==========\n")

total_training_cost = (
    df["training_cost_in_Rupees"].sum()
)

average_training_cost = (
    df["training_cost_in_Rupees"].mean()
)

print(
    "Total Training Cost:",
    round(total_training_cost, 2)
)

print(
    "Average Training Cost:",
    round(average_training_cost, 2)
)


# --------------------------------------------------
# 7. Training Cost by Program
# --------------------------------------------------

print("\n========== TRAINING COST BY PROGRAM ==========\n")

training_cost_by_program = (
    df.groupby("training_program_name")[
        "training_cost_in_Rupees"
    ]
    .sum()
    .sort_values(ascending=False)
)

print(training_cost_by_program)


# --------------------------------------------------
# 8. Training Duration
# --------------------------------------------------

print("\n========== TRAINING DURATION ==========\n")

print(
    "Average Training Duration:",
    round(df["training_duration_days"].mean(), 2),
    "days"
)


# --------------------------------------------------
# 9. Duration by Program
# --------------------------------------------------

duration_by_program = (
    df.groupby("training_program_name")[
        "training_duration_days"
    ]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Duration by Program:")
print(duration_by_program)


# --------------------------------------------------
# 10. Save results
# --------------------------------------------------

training_cost_by_program.to_csv(
    OUTPUT_DIR / "training_cost_by_program.csv"
)

duration_by_program.to_csv(
    OUTPUT_DIR / "training_duration_by_program.csv"
)

print("\nTraining analysis completed.")