import random

num_steps = 100
position = 0
positions = [position]

for _ in range(num_steps):
    step = random.choice([-1, 1])
    position += step
    positions.append(position)