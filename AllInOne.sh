#!/bin/bash

clear

echo "


  __  __ _  ____  ____  ____  ___      ____  ____   __     __  ____  ____ 
 (  )(  ( \(  __)/ _  \(__  )/ __)    (  _ \(  _ \ /  \  _(  )(  __)(_  _)
  )( /    / ) _) ) _  (  / /(  _ \     ) __/ )   /(  O )/ \) \ ) _)   )(  
 (__)\_)__)(__)  \____/ (_/  \___/    (__)  (__\_) \__/ \____/(____) (__) 



"

echo "If you meet an error with Python libraries, feel free to add 'pip install <yourlibraryname>' to the dockerfile !"

if [ $# -eq 0 ]; then
    echo "Usage: $0 <python_program>"
    exit 1
fi

python_program="$1"

if [ ! -f "$python_program" ]; then
    echo "Error: File '$python_program' not found."
    exit 1
fi

if [[ ! "$python_program" =~ \.py$ ]]; then
    echo "Error: '$python_program' is not a valid Python program (missing .py extension)."
    exit 1
fi

docker build PythonDockerfile/ -t temp 1>/dev/null

docker run -d --name memory_guesser -it temp:latest /bin/bash 1>/dev/null

docker cp $python_program memory_guesser:/app/prog.py 1>/dev/null

docker exec memory_guesser chmod +x /app/run.sh 1>/dev/null

docker exec memory_guesser /app/run.sh /app/prog.py -y

docker stop memory_guesser 1>/dev/null

docker container rm memory_guesser 1>/dev/null
