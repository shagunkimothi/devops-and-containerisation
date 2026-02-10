# Base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /home/app

# Copy python file into container
COPY app.py .

# Install dependency
RUN pip install numpy

# Run the application
CMD ["python", "app.py"]