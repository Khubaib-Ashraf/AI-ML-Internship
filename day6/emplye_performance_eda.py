import pandas as pd
import numpy as np

# ==========================
# Read Dataset
# ==========================

df = pd.read_csv(r"C:\Users\PCP\Desktop\day6\employee_performance_raw_dataset.csv")
print("Dataset Loaded Successfully\n")

# ==========================
# Display Dataset
# ==========================

print(df.head())

print("\nDataset Information")
print(df.info())

print("\nColumn Names")
print(df.columns.tolist())

# ==========================
# Remove Duplicate Records
# ==========================

duplicates = df.duplicated().sum()
print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

print("Rows After Removing Duplicates:", len(df))

# ==========================
# Clean Numeric Columns
# ==========================

numeric_columns = [
    "Age",
    "Experience (Years)",
    "Monthly Salary",
    "Attendance (%)",
    "Performance Score",
    "Overtime Hours",
    "Projects Completed",
    "Training Hours",
    "Remote Work Days"
]
for col in numeric_columns:
    if col in df.columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("$", "", regex=False)
            .str.replace("%", "", regex=False)
            .str.replace("years", "", case=False, regex=False)
            .str.replace("year", "", case=False, regex=False)
            .str.strip()
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")
# ==========================
# Missing Values
# ==========================
print("\nMissing Values Before Cleaning")
print(df.isnull().sum())
for col in numeric_columns:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())
if "Department" in df.columns:
    df["Department"] = df["Department"].fillna("Unknown")
if "Gender" in df.columns:
    df["Gender"] = df["Gender"].fillna("Unknown")
if "Notes" in df.columns:
    df["Notes"] = df["Notes"].fillna("No Remarks")
# ==========================
# Data Consistency
# ==========================
if "Department" in df.columns:
    df["Department"] = df["Department"].str.title()
if "Gender" in df.columns:
    df["Gender"] = df["Gender"].str.title()
if "Employee ID" in df.columns:
    df["Employee ID"] = df["Employee ID"].astype(str)
# ==========================
# Remove Unnecessary Columns
# ==========================
if "Notes" in df.columns:
    df.drop(columns=["Notes"], inplace=True)
# ==========================
# Handle Salary Outliers
# ==========================
if "Monthly Salary" in df.columns:
    Q1 = df["Monthly Salary"].quantile(0.25)
    Q3 = df["Monthly Salary"].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[
        (df["Monthly Salary"] >= lower) &
        (df["Monthly Salary"] <= upper)
    ]
# ==========================
# Final Data Types
# ==========================
print("\nFinal Data Types")
print(df.dtypes)
# ==========================
# Final Missing Values
# ==========================
print("\nMissing Values After Cleaning")
print(df.isnull().sum())
# ==========================
# Save Cleaned Dataset
# ==========================
df.to_csv(
    r"C:\Users\PCP\Desktop\day6\employee_performance_cleaned_dataset.csv",
    index=False
)
print("\nCleaning Completed Successfully")
print("Final Rows:", len(df))
print("\nCleaned dataset saved successfully.")
