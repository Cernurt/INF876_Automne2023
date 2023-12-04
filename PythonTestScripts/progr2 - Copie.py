import pandas as pd

# Créer un DataFrame avec des données fictives
data = {'Nom': ['Alice', 'Bob', 'Charlie'],
        'Âge': [25, 30, 22],
        'Score': [85, 92, 88]}

df = pd.DataFrame(data)

# Afficher le DataFrame
print("DataFrame:\n", df)

# Calculer la moyenne des scores
mean_score = df['Score'].mean()
print(f"Moyenne des scores: {mean_score}")