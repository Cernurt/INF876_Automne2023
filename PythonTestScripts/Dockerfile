# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app
#Add all examples + Inspector.py to run SAAF
COPY . /app
# Run the specified Python script when the container launches
RUN pip install pylint && \
pip install bandit

ENTRYPOINT echo Ryan
