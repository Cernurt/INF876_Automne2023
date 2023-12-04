import numpy as np
import time

# Create a large array to consume memory
large_array = np.random.rand(2500, 2500)

# Perform a time-consuming operation on the array
start_time = time.time()
result = np.linalg.eigvals(large_array)
end_time = time.time()

# Print the execution time
print(f"Execution time: {end_time - start_time} seconds")
