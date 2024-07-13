import pandas as pd
import itertools

# Read data from Excel file
df = pd.read_excel("D:/Kiet/for major project/Testcase (1).xlsx")

# Extract test cases from Excel file
test_cases = df["Test Case ID 3"].tolist()

# Generate all possible permutations of test cases
permutations = list(itertools.permutations(test_cases))

# Define fitness function
def fitness_function(permutation):
    total_sum = 0
    for case in permutation:
        for char in str(case):
            total_sum += ord(char)
    return total_sum

# Initialize variables to store the best individual and its fitness score
best_individual = None
best_fitness = float('-inf')  # Initialize with negative infinity

# Loop through each permutation and find the best individual
for i, permutation in enumerate(permutations):
    fitness = fitness_function(permutation)
    print(f"Permutation {i+1}: {permutation}, Fitness: {fitness}")
    # Update best individual if current permutation has higher fitness
    if fitness > best_fitness:
        best_individual = permutation
        best_fitness = fitness

# Display the best individual
print("Best Individual:", best_individual)
print("Fitness Score:", best_fitness)
