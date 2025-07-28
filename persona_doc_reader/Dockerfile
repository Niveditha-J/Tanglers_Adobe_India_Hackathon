FROM --platform=linux/amd64 python:3.10

WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
