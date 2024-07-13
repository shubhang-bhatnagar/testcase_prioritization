import pandas as pd
import itertools
import numpy as np

def calculate_hypervolume(points):
    """Calculate the hypervolume of a set of points."""
    # Sort the points by their last coordinate in ascending order
    sorted_points = sorted(points, key=lambda x: x[-1])

    # Initialize hypervolume to 0
    hypervolume = 0

    # Iterate over the sorted points and calculate hypervolume incrementally
    for i in range(len(sorted_points) - 1):
        hypervolume += (sorted_points[i+1][-1] - sorted_points[i][-1]) * \
                       np.prod(sorted_points[i][:-1])

    return hypervolume

# Read data from Excel file
df = pd.read_excel("D:/Kiet/for major project/Testcase (1).xlsx")

# Extract test cases from Excel file
test_cases = df["Test Case ID 3"].tolist()

# Generate all possible permutations of test cases
permutations = list(itertools.permutations(test_cases))

# Calculate hypervolume for each permutation
hypervolume_per_permutation = []
for i, permutation in enumerate(permutations):
    # Calculate hypervolume for the current permutation
    hypervolume = sum(permutation)  # Replace this with your own logic
    hypervolume_per_permutation.append((permutation, hypervolume))

# Sort permutations by hypervolume in descending order
sorted_permutations = sorted(hypervolume_per_permutation, key=lambda x: x[1], reverse=True)

# Display the sorted permutations with hypervolume
for i, (permutation, hypervolume) in enumerate(sorted_permutations):
    print(f"Permutation {i+1}: {permutation}, Hypervolume: {hypervolume}")
