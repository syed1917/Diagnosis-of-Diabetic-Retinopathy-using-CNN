# Use an official Python runtime as the base image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Copy application files (main app)
COPY app.py /app/

# Copy the TensorFlow model
COPY diabetic_retinopathy_model.h5 /app/

# Copy the database
COPY users.db /app/

# Copy the requirements file
COPY requirements.txt /app/

# Copy the templates (HTML files)
COPY templates/ /app/templates/

# Copy static files (CSS, JS, images)
COPY static/ /app/static/

# Copy existing records (pdf, images)
COPY uploads/ /app/uploads/

# Ensure the 'uploads' directory exists
RUN mkdir -p /app/uploads

# Install system dependencies (for TensorFlow, SQLite, and image processing)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
