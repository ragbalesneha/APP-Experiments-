import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Generate a DataFrame with Name, Age, Department, and Salary (including an outlier for demonstration)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Age': [25, 32, 28, 45, 30, 26, 35, 29, 41, 38],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Salary': [50000, 60000, 55000, 120000, 52000, 58000, 63000, 49000, 115000, 61000] # 120k and 115k act as outliers
}

df = pd.DataFrame(data)
print("--- 1. Original DataFrame ---")
print(df)
print("\n")

# Task 2: Compute Mean, median, and standard deviation of salary
mean_salary = df['Salary'].mean()
median_salary = df['Salary'].median()
std_salary = df['Salary'].std()

print("--- 2. Salary Statistics ---")
print(f"Mean Salary: {mean_salary:.2f}")
print(f"Median Salary: {median_salary:.2f}")
print(f"Standard Deviation of Salary: {std_salary:.2f}\n")

# Task 3: Detect and remove outliers using the IQR (Interquartile Range) method
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter out the outliers
df_filtered = df[(df['Salary'] >= lower_bound) & (df['Salary'] <= upper_bound)]

print(f"--- 3. Outlier Detection (IQR Method) ---")
print(f"Q1: {Q1}, Q3: {Q3}, IQR: {IQR}")
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
print("\nDataFrame after removing outliers:")
print(df_filtered)
print("\n")

# Task 4: Plot salary distribution (boxplot & histogram)
plt.figure(figsize=(12, 5))

# Boxplot
plt.subplot(1, 2, 1)
sns.boxplot(y=df['Salary'], color='skyblue')
plt.title('Salary Boxplot (Detecting Outliers)')
plt.ylabel('Salary')

# Histogram
plt.subplot(1, 2, 2)
sns.histplot(df['Salary'], kde=True, color='purple', bins=5)
plt.title('Salary Distribution Histogram')
plt.xlabel('Salary')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()