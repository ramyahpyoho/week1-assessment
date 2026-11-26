
# Task 3: NumPy, Pandas and Data Visualization

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# PART 1: NUMPY

# Create a 4x3 NumPy array
scores = np.array([
    [75, 80, 85],
    [90, 88, 92],
    [65, 70, 72],
    [85, 90, 95]
])

print("Original Array:")
print(scores)

# Display array shape
print("\nArray Shape:", scores.shape)

# Average of each row
print("\nRow Averages:")
print(np.mean(scores, axis=1))

# Average of each column
print("\nColumn Averages:")
print(np.mean(scores, axis=0))

# Broadcasting: Add 5 to every value
print("\nAfter Adding 5:")
print(scores + 5)

# Weighted scores using np.dot
weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(scores, weights)

print("\nWeighted Scores:")
print(weighted_scores)



# PART 2: PANDAS

# Read employee data
df = pd.read_csv("task2/employees.csv")

# Display first 5 rows
print("\nFirst 5 Employees:")
print(df.head())

# Display DataFrame information
print("\nDataFrame Information:")
df.info()

# Statistical summary
print("\nStatistical Description:")
print(df.describe())

# Select rows and columns using loc
print("\nUsing loc:")
print(df.loc[0:2, ["name", "salary"]])

# Select rows and columns using iloc
print("\nUsing iloc:")
print(df.iloc[0:3, 0:4])

# Filter employees earning above 50000
print("\nEmployees earning above 50000:")
print(df[df["salary"] > 50000])

# Filter employees from Chennai
print("\nEmployees from Chennai:")
print(df[df["city"] == "Chennai"])





# PART 3: DATA CLEANING

# Make a copy of employee data
dirty_df = df.copy()

# Add 2 missing salaries
dirty_df.loc[0, "salary"] = np.nan
dirty_df.loc[1, "salary"] = np.nan

# Add one duplicate row
dirty_df = pd.concat(
    [dirty_df, dirty_df.iloc[[2]]],
    ignore_index=True
)

print("\nData before cleaning:")
print(dirty_df)

# Fill missing salaries using median
median_salary = dirty_df["salary"].median()
dirty_df["salary"] = dirty_df["salary"].fillna(median_salary)

# Remove duplicate rows
dirty_df = dirty_df.drop_duplicates()

# Correct data types
dirty_df["salary"] = dirty_df["salary"].astype(int)
dirty_df["id"] = dirty_df["id"].astype(int)

print("\nData after cleaning:")
print(dirty_df)

print("\nMissing values:")
print(dirty_df.isnull().sum())

print("\nDuplicate rows:", dirty_df.duplicated().sum())


# PART 4: GROUPING AND AGGREGATION

print("\nDepartment Summary:")

department_summary = dirty_df.groupby("department").agg(
    headcount=("name", "count"),
    average_salary=("salary", "mean"),
    maximum_salary=("salary", "max")
)

print(department_summary)

# Read department master data
departments = pd.read_csv("task3/departments.csv")

print("\nDepartment Master Data:")
print(departments)

# PART 5: MERGING

# Inner merge
inner_merge = pd.merge(
    dirty_df, departments, on="department", how="inner"
)
print("\nInner Merge:")
print(inner_merge)

# Left merge
left_merge = pd.merge(
    dirty_df, departments, on="department", how="left"
)
print("\nLeft Merge:")
print(left_merge)

# Outer merge
outer_merge = pd.merge(
    dirty_df, departments, on="department", how="outer"
)
print("\nOuter Merge:")
print(outer_merge)

# Departments without employees
employee_departments = set(dirty_df["department"])
all_departments = set(departments["department"])

empty_departments = all_departments - employee_departments

print("\nDepartments without employees:")
print(empty_departments)



# PART 6: DATA VISUALIZATION

import os

# Create reports folder if it does not exist
os.makedirs("task3/reports", exist_ok=True)

# Chart 1: Bar chart - Average salary by department
avg_salary = dirty_df.groupby("department")["salary"].mean()

plt.figure(figsize=(8, 5))
avg_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.tight_layout()
plt.savefig("task3/reports/bar_chart.png")
plt.show()

print("Insight: The IT department has the highest average salary.")

# Chart 2: Histogram - Salary distribution
plt.figure(figsize=(8, 5))
plt.hist(dirty_df["salary"], bins=5, edgecolor="black")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.tight_layout()
plt.savefig("task3/reports/histogram.png")
plt.show()

print("Insight: Most employee salaries are concentrated around the middle salary range.")

# Chart 3: Scatter plot - Employee ID vs Salary
plt.figure(figsize=(8, 5))
plt.scatter(dirty_df["id"], dirty_df["salary"])
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("task3/reports/scatter_plot.png")
plt.show()

print("Insight: Employee salaries vary across employee IDs.")

# Chart 4: Line chart - Employee salary trend
plt.figure(figsize=(8, 5))
plt.plot(dirty_df["id"], dirty_df["salary"], marker="o", label="Salary")
plt.title("Employee Salary Trend")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend()
plt.tight_layout()
plt.savefig("task3/reports/line_chart.png")
plt.show()

print("Insight: Salary changes across employees rather than increasing consistently.")
