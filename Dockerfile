# Use a base image with Python
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (Flask default is 5000)
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
