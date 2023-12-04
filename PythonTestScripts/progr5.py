import math
import random

point1 = (random.uniform(0, 10), random.uniform(0, 10))
point2 = (random.uniform(0, 10), random.uniform(0, 10))

distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

print("Point 1:", point1)
print("Point 2:", point2)
print("Distance euclidienne:", distance)