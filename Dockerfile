FROM python:3.11-slim

WORKDIR /app

# Optimization: Only copy requirements first
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Match your filename!
CMD ["python", "app.py"]