import pandas as pd
import itertools

# Read data from Excel file
df = pd.read_excel("D:/Kiet/for major project/Testcase (1).xlsx")

# Extract test cases from Excel file
test_cases = df["Test Case ID 3"].tolist()

# Generate all possible permutations of test cases
permutations = list(itertools.permutations(test_cases))

# Display the permutations
for i, permutation in enumerate(permutations):
    print(f"Permutation {i+1}: {permutation}")
