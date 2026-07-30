import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Cleaned Dataset
df = pd.read_csv(r"C:\Users\PCP\Desktop\day6\employee_performance_cleaned_dataset.csv")
# Summary Statistics
print(df.describe())
# Correlation
print(df.corr(numeric_only=True))
# Department with Highest Average Performance
dept = df.groupby("Department")["Performance Score"].mean()
print("\nAverage Performance by Department")
print(dept)
print("\nBest Department")
print(dept.idxmax())
# Attendance Below 75%
low = df[df["Attendance (%)"] < 75]
print("\nEmployees with Attendance Below 75%")
print(low)
# Performance Index
df["Performance Index"] = (
    df["Performance Score"] * 0.5
    + df["Projects Completed"] * 2
    + df["Attendance (%)"] * 0.3
)
# Promotion System
def promotion(row):
    if (
        row["Performance Index"] >= 80
        and row["Attendance (%)"] >= 90
        and row["Projects Completed"] >= 8
    ):
        return "Promoted"
    elif (
        row["Performance Index"] >= 60
        and row["Training Hours"] >= 20
    ):
        return "Requires Training"
    else:
        return "Needs Improvement"
df["Promotion Status"] = df.apply(promotion, axis=1)
# Save Updated Dataset
df.to_csv("employee_performance_final_dataset.csv", index=False)

# Visualization 1
plt.figure(figsize=(8,5))
sns.countplot(
    data=df,
    x="Department",
    hue="Department",
    palette="Set2",
    legend=False
)
plt.title("Employees in Each Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()
# Visualization 2
plt.figure(figsize=(8,5))
plt.hist(
    df["Monthly Salary"],
    bins=10,
    color="skyblue",
    edgecolor="black"
)
plt.axvline(
    df["Monthly Salary"].mean(),
    color="red",
    linestyle="--",
    linewidth=2,
    label="Average Salary"
)
plt.title("Monthly Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
# Visualization 3
plt.figure(figsize=(6,5))
sns.boxplot(
    y=df["Performance Score"],
    color="lightgreen"
)
plt.title("Performance Score Distribution")
plt.ylabel("Performance Score")
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.show()
# Visualization 4
plt.figure(figsize=(8,5))
sns.scatterplot(
    data=df,
    x="Attendance (%)",
    y="Performance Score",
    hue="Department",
    s=100
)
plt.title("Attendance vs Performance Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Performance Score")
plt.grid(alpha=0.3)
plt.show()
# Visualization 5
salary_exp = df.groupby("Experience (Years)")["Monthly Salary"].mean().reset_index()
plt.figure(figsize=(8,5))
plt.plot(
    salary_exp["Experience (Years)"],
    salary_exp["Monthly Salary"],
    marker="o",
    linewidth=2,
    color="green"
)
plt.title("Average Salary by Experience")
plt.xlabel("Experience (Years)")
plt.ylabel("Average Salary")
plt.grid(True)
plt.show()
# Visualization 6
plt.figure(figsize=(10,8))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="YlGnBu",
    linewidths=0.5,
    fmt=".2f"
)
plt.title("Correlation Between Numerical Features")
plt.show()
# Visualization 7
dept = df.groupby("Department")["Performance Score"].mean().sort_values()

plt.figure(figsize=(8,5))

bars = plt.bar(
    dept.index,
    dept.values,
    color=["skyblue","orange","green","red","purple"]
)

plt.title("Average Performance Score by Department")
plt.xlabel("Department")
plt.ylabel("Average Score")
plt.grid(axis="y", alpha=0.3)
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height() + 0.3,
        f"{bar.get_height():.1f}",
        ha="center"
    )
plt.show()
# Visualization 8
promotion = df["Promotion Status"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    promotion,
    labels=promotion.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=["green","orange","red"]
)
plt.title("Promotion Eligibility Status")
plt.show()