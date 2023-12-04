from radon.complexity import cc_visit
from radon.raw import analyze
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import os

def get_python_files(directory):
    python_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                python_files.append(file_path)
    
    return python_files

def extract_features(script):
    with open(script, 'r', encoding='utf-8') as file:
        script_code = file.read()

    # Nombre de lignes de code (LOC)
    loc = script_code.count('\n') + 1

    # Complexité cyclomatique totale
    complexity = analyze(script_code).total_complexity

    # Moyenne des complexités cyclomatiques par fonction
    cc_ranks = [node.complexity for node in cc_visit(script_code)]
    avg_cc_rank = sum(cc_ranks) / len(cc_ranks) if cc_ranks else 0

    return {
        'loc': loc,
        'total_complexity': complexity,
        'avg_cc_rank': avg_cc_rank
    }

execution_times = [10, 15, 20]  # en secondes
memory_usage = [100, 150, 200]  # en mégaoctets

directory_path = "C:/Users:table/Downloads/Python-master"

# Génération de données d'exemple (à remplacer par vos propres données)
scripts = get_python_files(directory_path)

if not scripts:
    print("No Python files found in the specified directory.")
else:
    # Transformation des scripts en caractéristiques
    X = np.array([extract_features(script) for script in scripts])
    print(X)
    y = np.array(list(zip(execution_times, memory_usage)))

    # Check if X is empty before attempting to split
    if not X.any():
        print("No features extracted from the Python files. Check your extract_features function.")
    else:
        # Division des données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # ... (continue with the rest of your code)
        # Ensure that you define and fit your models inside this block

        # Entraînement du modèle de régression linéaire pour le temps d'exécution
        model_execution_time = LinearRegression()
        model_execution_time.fit(X_train, y_train[:, 0])  # Première colonne pour le temps d'exécution

        # Prédiction sur l'ensemble de test pour le temps d'exécution
        y_pred_execution_time = model_execution_time.predict(X_test)

        # Entraînement du modèle de régression linéaire pour la mémoire
        model_memory_usage = LinearRegression()
        model_memory_usage.fit(X_train, y_train[:, 1])  # Deuxième colonne pour la mémoire

        # Prédiction sur l'ensemble de test pour la mémoire
        y_pred_memory_usage = model_memory_usage.predict(X_test)


# Évaluation de la performance du modèle pour le temps d'exécution
mse_execution_time = mean_squared_error(y_test[:, 0], y_pred_execution_time)
print(f"Mean Squared Error (Execution Time): {mse_execution_time}")

# Évaluation de la performance du modèle pour la mémoire
mse_memory_usage = mean_squared_error(y_test[:, 1], y_pred_memory_usage)
print(f"Mean Squared Error (Memory Usage): {mse_memory_usage}")

# Utilisez les modèles pour prédire le temps d'exécution et la mémoire RAM d'un nouveau script
new_script = "nouveau_script.py"
new_script_features = extract_features(new_script)
prediction_execution_time = model_execution_time.predict([new_script_features])
prediction_memory_usage = model_memory_usage.predict([new_script_features])

print(f"Prédiction du temps d'exécution pour {new_script}: {prediction_execution_time[0]} secondes")
print(f"Prédiction de la mémoire RAM pour {new_script}: {prediction_memory_usage[0]} mégaoctets")
