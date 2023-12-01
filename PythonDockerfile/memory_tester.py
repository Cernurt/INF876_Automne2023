import resource
import subprocess
import time
import sys 


memory_setting = int(sys.argv[1])
python_code = sys.argv[2]

resource.setrlimit(resource.RLIMIT_AS, (memory_setting * 1024 * 1024, memory_setting * 1024 * 1024)) 

start_time = time.time()
subprocess.run(["python3", python_code])
end_time = time.time()

print(f"Timing program : {resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime}")
