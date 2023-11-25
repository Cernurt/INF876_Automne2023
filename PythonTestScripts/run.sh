#!/bin/bash


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

echo "Running bandit on $python_program..."

bandit "$python_program"
