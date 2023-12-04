import random
import statistics

data = [random.randint(1, 10) for _ in range(30)]

window_size = 3
moving_averages = [statistics.mean(data[i:i+window_size]) for i in range(len(data)-window_size+1)]

print("Liste de données:", data)
print(f"Moyenne mobile avec fenêtre de taille {window_size}:", moving_averages)