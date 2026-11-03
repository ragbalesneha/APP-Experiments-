import pandas as pd
import numpy as np

# Task 1: Create a DataFrame with patient info (including some missing values in Age, Weight, and Name)
data = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva'],
    'Age': [28, np.nan, 34, 45, 29],
    'Weight': [62.5, 75.0, 80.2, np.nan, 55.4],
    'Blood_Pressure': ['120/80', '130/85', np.nan, '140/90', '125/82']
}

df = pd.DataFrame(data)
print("--- 1. Original DataFrame with Missing Values ---")
print(df)
print("\n")

# Task 3: Drop rows where Name is missing (doing this before imputation or right after as per workflow preference)
df_cleaned_names = df.dropna(subset=['Name'])

# Task 2: Fill missing numerical values using mean imputation
# Select only numerical columns for mean imputation
numerical_cols = ['Age', 'Weight']
for col in numerical_cols:
    mean_value = df_cleaned_names[col].mean()
    df_cleaned_names[col] = df_cleaned_names[col].fillna(mean_value)

print("--- Final DataFrame (Name dropped & Missing numerical values filled with mean) ---")
print(df_cleaned_names)