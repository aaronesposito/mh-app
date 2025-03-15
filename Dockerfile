# Use an official Python runtime
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Create a virtual environment and install dependencies
RUN python -m venv venv && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5001

# Ensure the container uses the virtual environment by default
ENV PATH="/app/venv/bin:$PATH"

# Start the application using Waitress
CMD ["waitress-serve", "--host=0.0.0.0", "--port=5001", "app:app"]