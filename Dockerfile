# AgroScan AI - Dockerfile for Google Cloud Run & Container Deployments
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Install required system libraries for OpenCV and image operations
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install PyTorch CPU first to leverage Docker layer caching
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Copy requirements and install remaining dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy application source code
COPY . .

# Expose target port
EXPOSE 8080

# Production WSGI server command for Google Cloud Run
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 120 app:app
