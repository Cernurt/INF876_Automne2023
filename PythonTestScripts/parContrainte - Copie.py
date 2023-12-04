import random
import statistics

data = [random.randint(1, 100) for _ in range(50)]

mean_value = statistics.mean(data)
median_value = statistics.median(data)
std_deviation = statistics.stdev(data)

print("Données aléatoires:", data)
print("Moyenne:", mean_value)
print("Médiane:", median_value)
print("Écart-type:", std_deviation)
