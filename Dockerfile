# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies inside a virtual environment
RUN python -m venv venv \
    && . venv/bin/activate \
    && pip install --no-cache-dir -r requirements.txt

# Expose the port that the app runs on
EXPOSE 5001

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=dev
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH" 

# uncomment for prod
# Start the application using Waitress
CMD ["venv/bin/waitress-serve", "--host=0.0.0.0", "--port=5001", "app:app"]

# Uncomment for dev
# CMD ["venv/bin/flask", "run", "--host=0.0.0.0", "--port=5001", "--debug"]