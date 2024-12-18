FROM python:3.9

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install TensorFlow
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt --break-system-packages

# Copy application code (if any)
# COPY . /usr/src/app

# Default command (adjust as needed)
CMD ["python3"]