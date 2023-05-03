# Use the official Python image as the base image
FROM python:3.10-slim

# Copy the application code and requirements.txt to the container
COPY app /app
COPY requirements.txt /app

# Set the working directory
WORKDIR /app

# Upgrade pip and install required packages
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the .env file to the container (if needed)
COPY .env /app

# Set the entry point for the container
ENTRYPOINT ["python", "main.py"]
