import random
import math
import statistics

mean = 50
std_dev = 10

data = [random.gauss(mean, std_dev) for _ in range(100)]

mean_value = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("Données générées:", data)
print("Moyenne:", mean_value)
print("Écart-type:", std_deviation)