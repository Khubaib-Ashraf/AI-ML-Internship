# Import pandas
import pandas as pd

# Import numpy
import numpy as np

# Read dataset
df = pd.read_csv("interns_dataset.csv")

# Display first five rows
print(df.head())
# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Check missing values
print(df.isnull().sum())
# Replace missing values with column average
df.fillna(df.mean(numeric_only=True), inplace=True)

df["Performance Score"] = (
    (df["Quiz Score"] * 0.35)
    + (df["Attendance Percentage"] * 0.25)
    + (df["Tasks Completed"] * 2)
    + (df["Daily Learning Hours"] * 5)
    - (df["Average Submission Time"] * 2)
)
def performance(score):

    if score >= 90:
        return "Excellent"

    elif score >= 75:
        return "Good"

    elif score >= 60:
        return "Average"

    else:
        return "Needs Improvement"

df["Performance Level"] = df["Performance Score"].apply(performance)
top5 = df.sort_values(
    by="Performance Score",
    ascending=False
).head(5)

print(top5)
bottom5 = df.sort_values(
    by="Performance Score"
).head(5)

print(bottom5)
department = df.groupby("Department")["Performance Score"].mean()

print(department)

print()

print("Best Department")

print(department.idxmax())
average_attendance = np.mean(df["Attendance Percentage"])

print("Average Attendance")

print(average_attendance)
mentor = df[
    (df["Attendance Percentage"] < 70) |
    (df["Quiz Score"] < 50) |
    (df["Tasks Completed"] < df["Tasks Assigned"] / 2)
]

print(mentor)
def recommendation(row):

    message = []

    if row["Attendance Percentage"] < 70:
        message.append("Improve attendance")

    if row["Quiz Score"] < 50:
        message.append("Practice programming")

    if row["Tasks Completed"] < row["Tasks Assigned"] / 2:
        message.append("Complete pending tasks")

    if row["Daily Learning Hours"] < 2:
        message.append("Increase learning hours")

    if len(message) == 0:
        return "Excellent performance"

    return ", ".join(message)

df["Recommendation"] = df.apply(recommendation, axis=1)
print("========== SUMMARY ==========")

print()

print("Total Interns")

print(len(df))

print()

print("Average Attendance")

print(df["Attendance Percentage"].mean())

print()

print("Average Quiz Score")

print(df["Quiz Score"].mean())

print()

print("Average Learning Hours")

print(df["Daily Learning Hours"].mean())

print()

print("Best Department")

print(df.groupby("Department")["Performance Score"].mean().idxmax())

print()

print("Performance Levels")

print(df["Performance Level"].value_counts())
df.to_csv(
    "interns_dataset_updated.csv",
    index=False
)
with open("analysis_report.txt", "w") as file:

    file.write("Internship Performance Analysis Report\n\n")

    file.write("Total Interns\n")
    file.write(str(len(df)))
    file.write("\n\n")

    file.write("Average Attendance\n")
    file.write(str(df["Attendance Percentage"].mean()))
    file.write("\n\n")

    file.write("Average Quiz Score\n")
    file.write(str(df["Quiz Score"].mean()))
    file.write("\n\n")

    file.write("Performance Levels\n")
    file.write(str(df["Performance Level"].value_counts()))
