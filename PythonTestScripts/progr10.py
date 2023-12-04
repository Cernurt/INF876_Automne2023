import math
import random

# Générer des données en utilisant la fonction logarithmique
x_values = [i for i in range(1, 101)]
y_values = [math.log(x) for x in x_values]
lambda_param = 0.5
coin_tosses = [random.choice(['Tête', 'Pile']) for _ in range(50)]
# Générer des données suivant une distribution exponentielle
data = [random.expovariate(lambda_param) for _ in range(1000)]
print("Résultats des lancers de pièce de monnaie:", coin_tosses)