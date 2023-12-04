import random
import statistics

# Générer deux ensembles de données
data1 = [random.randint(1, 10) for _ in range(20)]
data2 = [x + random.uniform(-1, 1) for x in data1]

# Calculer la corrélation entre les deux ensembles
correlation = statistics.correlation(data1, data2)

print("Ensemble de données 1:", data1)
print("Ensemble de données 2:", data2)
print("Corrélation entre les deux ensembles:", correlation)