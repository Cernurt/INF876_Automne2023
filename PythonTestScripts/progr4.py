import random
import statistics

num_simulations = 10000
dice_rolls = [random.randint(1, 6) for _ in range(num_simulations)]

for i in range(1, 7):
    probability = dice_rolls.count(i) / num_simulations
    print(f"Probabilité d'obtenir {i} : {probability:.4f}")