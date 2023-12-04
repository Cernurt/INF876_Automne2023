#!/bin/bash


clear

echo "


  __  __ _  ____  ____  ____  ___      ____  ____   __     __  ____  ____ 
 (  )(  ( \(  __)/ _  \(__  )/ __)    (  _ \(  _ \ /  \  _(  )(  __)(_  _)
  )( /    / ) _) ) _  (  / /(  _ \     ) __/ )   /(  O )/ \) \ ) _)   )(  
 (__)\_)__)(__)  \____/ (_/  \___/    (__)  (__\_) \__/ \____/(____) (__) 



"

if [ $# -eq 0 ]; then
    echo "Usage: $0 <python_program> (-y)"
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


if [[ $2 = "-y" ]]; then 
    autoskip=1
else 
    autoskip=O
fi

echo "-------------------------------------------------------------"

echo "Running pylint on $python_program..."
pylint "$python_program"

echo "-------------------------------------------------------------"

echo "Running bandit on $python_program..."

bandit "$python_program"

echo "-------------------------------------------------------------"
echo " "


if [[ $autoskip = 1 ]]; then

    answer="y"

else
    echo "Do you want to run a dynamic analysis on the python program? (y/n)"
    read answer
fi

if [ $answer = "y" ]; then
   
    echo -n "Running the Python script now " 
    
    
    scalene $python_program &
    PID=$!
    i=1
    sp="/-\|"
    echo -n ' '
    while [ -d /proc/$PID ]
    do
        sleep 0.3
        printf "\b${sp:i++%${#sp}:1}"
    done 

elif [ "$answer" = "n" ]; then
    echo "Okay, not running the Dynamic analysis..."
else
    echo "Invalid input. PLEASE enter 'y' or 'n'."
fi
