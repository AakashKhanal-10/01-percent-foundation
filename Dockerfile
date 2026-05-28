# Use the python-slim image as discussed
FROM python:3.11-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Use 'sed' to remove pywinpty before installing (the "Safety Net" approach)
RUN sed -i '/pywinpty/d' requirements.txt && \
    pip install --no-cache-dir -r requirements.txt

COPY . .
# Open the communication gateway port for FastAPI
EXPOSE 8000

CMD ["uvicorn","app:app","--host","0.0.0.0","--port", "8000"]