# Use Python base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 80

# Run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
