# Use official lightweight Python image
FROM python:3.12-slim

# Set work directory inside the container
WORKDIR /app

# Install system dependencies needed for MariaDB/MySQL client
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the API code
COPY . /app

# Environment variables
ENV FLASK_ENV=production \
    PYTHONUNBUFFERED=1

# Expose the API port
EXPOSE 8000

# Run the Flask app
CMD ["python", "run.py"]
