
FROM python:3.9-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Copy the requirements file into the image
COPY requirements.txt .

# Install pip and upgrade it to the latest version
RUN pip install --no-cache-dir --upgrade pip

# Create a virtual environment and set it as the PATH
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install system-level dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Install python packages from requirements.txt
RUN /venv/bin/pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the default command to run the application
CMD ["python", "project/main.py"]
