FROM python:3.11-slim

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory to /app
WORKDIR /app/app

# Copy the current directory contents into the container at /app
COPY . /app/app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV POSTGRES_HOST=your-postgres-host
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=your-db-name
ENV POSTGRES_USER=your-db-user
ENV POSTGRES_PASSWORD=your-db-password

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
