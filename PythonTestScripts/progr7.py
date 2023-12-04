import random

population = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.2, 0.2]

random_choice = random.choices(population, weights=weights, k=10)

print("Population:", population)
print("Poids associés:", weights)
print("Choix aléatoires pondérés:", random_choice)