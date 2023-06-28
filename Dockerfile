# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY . .

# Expose the port on which the application will run
EXPOSE 8080

# Run the application
CMD ["python", "blockchain_app.py"]
