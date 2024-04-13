# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster
LABEL authors="michele"

RUN apt-get update

RUN apt-get install git-all -y

# Set the working directory in the container to /app
WORKDIR /app

# Add current directory code to /app in container
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8736

# Run the application:
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8736"]