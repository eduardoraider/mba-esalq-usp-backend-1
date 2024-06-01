# Use Python 3.12 image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Install the requests library
RUN pip install requests

# Copy all your Python files to the container
COPY . src/app
