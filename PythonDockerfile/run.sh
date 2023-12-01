#!/bin/bash

clear

echo "


  __  __ _  ____  ____  ____  ___      ____  ____   __     __  ____  ____ 
 (  )(  ( \(  __)/ _  \(__  )/ __)    (  _ \(  _ \ /  \  _(  )(  __)(_  _)
  )( /    / ) _) ) _  (  / /(  _ \     ) __/ )   /(  O )/ \) \ ) _)   )(  
 (__)\_)__)(__)  \____/ (_/  \___/    (__)  (__\_) \__/ \____/(____) (__) 



"

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

echo "Running pylint on $python_program..."
pylint "$python_program"

echo "-------------------------------------------------------------"
echo "-------------------------------------------------------------"
echo "-------------------------------------------------------------"
echo "-------------------------------------------------------------"


echo "Running bandit on $python_program..."

bandit "$python_program"


echo "Do you want to run a dynamic analysis on the python program? (y/n)"
read answer


if [ "$answer" = "y" ]; then
    echo "Enter the memory you want to predict:"
    read number
    
    echo "Running the Python script..."
    if [[ $number =~ ^[0-9]+$ ]]; then
        echo "Running the Python script with the time needed for $number MB..."
    
        python3 main_ia_memory_predict.py $python_program $number 
    else
        echo "Invalid input. Please enter a valid number."
    fi
elif [ "$answer" = "n" ]; then
    echo "Okay, not running the Dynamic analysis."
else
    echo "Invalid input. Please enter 'yes' or 'no'."
fi
