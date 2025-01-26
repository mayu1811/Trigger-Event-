FROM python:3.10-slim

# Install Redis server
RUN apt-get update && \
    apt-get install -y redis-server && \
    apt-get clean

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the Redis and application ports
EXPOSE 6379
EXPOSE 5000

# Start Redis and the Python application
CMD service redis-server start && python run.py
