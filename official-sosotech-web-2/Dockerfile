# Base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
# COPY env.py .
COPY forms.py .
COPY requirements.txt .


# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the environment variables
ENV SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:Depay50#@10.1.0.119:3306/sosotechreal


# Run the Flask application
CMD ["python", "app.py"]

