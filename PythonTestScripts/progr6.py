import random
import math

initial_population = 100
growth_rate = 0.05
num_generations = 10

population = [initial_population * math.exp(growth_rate * i) for i in range(num_generations)]

print("Population initiale:", initial_population)
print("Taux de croissance:", growth_rate)
print("Population générée sur {} générations:".format(num_generations), population)