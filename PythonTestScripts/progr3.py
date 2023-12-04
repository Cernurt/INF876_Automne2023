import random
import math
import statistics

data = [random.randint(1, 10) for _ in range(20)]

sum_of_squares = sum(x ** 2 for x in data)

print("Liste de données:", data)
print("Somme des carrés des éléments:", sum_of_squares)