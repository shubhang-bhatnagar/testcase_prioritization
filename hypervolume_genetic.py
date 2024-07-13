import pandas as pd
import numpy as np
import random

# Read data from Excel file
df = pd.read_excel("D:/Kiet/for major project/Testcase (1).xlsx")

# Extract test cases from Excel file
test_cases = df["Test Case ID 3"].tolist()

# Define genetic algorithm parameters
population_size = 50
generations = 100
mutation_rate = 0.1


# Define fitness function using hypervolume calculation
def fitness_function(permutation):
    # Simplified hypervolume calculation
    reference_point = [max(permutation) + 1] * len(permutation)
    volumes = []

    for i in range(len(permutation)):
        dominated_space = [reference_point[j] - permutation[j] for j in range(len(permutation))]
        volumes.append(np.prod(dominated_space))

    return sum(volumes)  # Sum of volumes for all solutions


# Initialize population
population = [random.sample(test_cases, len(test_cases)) for _ in range(population_size)]

# Initialize variables to track the best individual and its generation
best_individual = None
best_fitness_score = -float('inf')
best_generation = -1

# Main genetic algorithm loop
for generation in range(generations):
    # Evaluate fitness of each individual in the population using hypervolume calculation
    fitness_scores = [fitness_function(individual) for individual in population]

    # Check for the best individual in the current generation
    current_best_fitness = max(fitness_scores)
    current_best_individual = population[fitness_scores.index(current_best_fitness)]

    # Update the best individual if the current one is better
    if current_best_fitness > best_fitness_score:
        best_fitness_score = current_best_fitness
        best_individual = current_best_individual
        best_generation = generation

    # Select parents for reproduction (tournament selection)
    parents = []
    for _ in range(population_size // 2):
        tournament_size = 5
        valid_indices = range(len(fitness_scores))  # Use the length of fitness_scores
        tournament_indices = random.sample(valid_indices, tournament_size)
        tournament_scores = [fitness_scores[i] for i in tournament_indices]
        parent_index = tournament_indices[tournament_scores.index(max(tournament_scores))]
        parents.append(population[parent_index])

    # Ensure number of parents is even
    if len(parents) % 2 != 0:
        parents.pop()  # Remove one parent if odd number of parents

    # Perform crossover (single-point crossover)
    offspring = []
    for i in range(0, len(parents), 2):
        parent1, parent2 = parents[i], parents[i + 1]
        crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.extend([child1, child2])

    # Perform mutation (swap mutation)
    for i in range(len(offspring)):
        if random.random() < mutation_rate:
            mutation_point1, mutation_point2 = random.sample(range(len(test_cases)), 2)
            offspring[i][mutation_point1], offspring[i][mutation_point2] = offspring[i][mutation_point2], offspring[i][
                mutation_point1]

    # Replace population with offspring
    population = offspring

# Display the best individual and its fitness score
print("Best Individual (Permutation):", best_individual)
print("Fitness Score:", best_fitness_score)



# Display the generation number of the best individual
print("Best Individual Found at Generation:", best_generation)
