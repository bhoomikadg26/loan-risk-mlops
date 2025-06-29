# Use official Python image
FROM python:3.10

# Set working directory in container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Start FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
