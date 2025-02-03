FROM python:3.11

# Set the working directory
WORKDIR /code

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# create static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8080

# Command to run django server using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "GenToken.wsgi:application"]
