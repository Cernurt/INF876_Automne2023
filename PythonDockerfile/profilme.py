import resource
import subprocess
import time

def run_program(memory_setting, program):

      
    start_time = time.time()
    
    process = subprocess.run(["python3", "memory_tester.py", str(memory_setting), program], capture_output=True,text=True)
    
    end_time = time.time()
    
    
    print(process.stdout[process.stdout.rfind("Timing program : ")+17: process.stdout.rfind("Timing program : ")+17 +9] )


    return float(process.stdout[process.stdout.rfind("Timing program : ")+17: process.stdout.rfind("Timing program : ")+17 +9])
    
    
    
#memory_settings = [128, 256, 512,768, 1024] 

def run_list(memory_settings, program): 
    cpu_usage_data=[]
    for memory_setting in memory_settings[::-1]:
        cpu_usage_data.append(run_program(memory_setting, program))
        print(memory_setting)
    return cpu_usage_data[::-1]


