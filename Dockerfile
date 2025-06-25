# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only necessary files
COPY app.py .
COPY animals.db .
COPY static/ ./static/
COPY templates/ ./templates/

# Install only needed packages
RUN pip install --no-cache-dir flask sqlalchemy

# Expose port Flask runs on
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
