from profilme import run_list
from resource import *

# prediction_script.py
from scipy.optimize import curve_fit
import numpy as np

import sys 


  
memory_settings = [128, 256, 512, 1024, 2048] 
program = sys.argv[1]
# Assuming you have collected CPU usage data from the profiling script
cpu_usage_data = np.array(run_list(memory_settings,program))


memory_settings = np.array(memory_settings)  # Adjust as needed


# Simple quadratic fit (you may need a more sophisticated model)
def quadratic_function(x, a, b, c):
    return a * x**2 + b * x + c


print('done')
#memory_settings, cpu_usage_data = [ 128,  256,  512, 1024], [0.188516, 0.136058, 0.089835, 0.039829]
print(memory_settings, cpu_usage_data)
print(getrusage(RUSAGE_SELF))

# Fit the data to the quadratic function
params, covariance = curve_fit(quadratic_function, memory_settings, cpu_usage_data)



# Predict CPU usage for a new memory setting (e.g., 768MB)
predicted_memory_setting = int(sys.argv[2])
predicted_cpu_usage = quadratic_function(predicted_memory_setting, *params)

print(f"Predicted CPU Usage for {predicted_memory_setting}MB: {predicted_cpu_usage:.5f} seconds")
