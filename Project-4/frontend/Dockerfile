# Use the official Python image as a parent image
FROM python:3

RUN pip install requests

WORKDIR /app

# Copy frontend.py into the container at /app
COPY frontend.py /app/frontend.py

# Run frontend.py when the container launches
CMD ["python", "/app/frontend.py", "&"]
