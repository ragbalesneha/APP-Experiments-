import numpy as np

# Set a random seed for reproducibility (optional)
np.random.seed(42)

# Task 1: Create a 1D NumPy array of 10 random integers between 80 and 150 (inclusive)
# Note: np.randint's high bound is exclusive, so we use 151.
heart_rates = np.random.randint(80, 151, size=10)
print("1. Heart rates for 10 minutes:", heart_rates)

# Task 2: Slice the array to get the first 5 minutes
first_5_minutes = heart_rates[:5]
print("2. First 5 minutes heart rates:", first_5_minutes)

# Task 3: Calculate the maximum, minimum, and average heart rate
max_hr = np.max(heart_rates)
min_hr = np.min(heart_rates)
avg_hr = np.mean(heart_rates)

print(f"3. Maximum Heart Rate: {max_hr}")
print(f"   Minimum Heart Rate: {min_hr}")
print(f"   Average Heart Rate: {avg_hr:.2f}")

# Task 4: Identify minutes where heart rate exceeded 120 bpm
# Using boolean indexing and finding indices where heart rate > 120
exceeded_120_indices = np.where(heart_rates > 120)[0]
exceeded_120_values = heart_rates[heart_rates > 120]

print("4. Minutes (indices + 1) where heart rate exceeded 120 bpm:")
for idx, hr in zip(exceeded_120_indices, exceeded_120_values):
    print(f"   Minute {idx + 1}: {hr} bpm")
    