# Use the python-slim image as discussed
FROM python:3.11-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Use 'sed' to remove pywinpty before installing (the "Safety Net" approach)
RUN sed -i '/pywinpty/d' requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]