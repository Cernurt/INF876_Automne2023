# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory to /app
WORKDIR /app

COPY . /app
# Run the specified Python script when the container launches
RUN pip install pylint && \
pip install bandit && \
pip install -U scalene
