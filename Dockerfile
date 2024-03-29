# Use an official Python runtime as a parent image
FROM python:3.12-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY gravityassistintcode.py test_intcode.py variables.py input.txt /app/

# Run script.py when the container launches
CMD ["sh", "-c", "python gravityassistintcode.py && python test_intcode.py"]