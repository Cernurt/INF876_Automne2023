import numpy as np

# Créer deux matrices
matrix_a = np.random.randint(1, 10, size=(3, 3))
matrix_b = np.random.randint(1, 10, size=(3, 3))

# Calculer la somme des matrices
sum_matrix = matrix_a + matrix_b

# Calculer le produit matriciel
product_matrix = np.dot(matrix_a, matrix_b)

print("Matrice A:\n", matrix_a)
print("Matrice B:\n", matrix_b)
print("Somme des matrices:\n", sum_matrix)
print("Produit matriciel:\n", product_matrix)