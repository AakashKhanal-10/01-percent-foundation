FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN useradd -m factory_worker
USER factory_worker
ENV ENGINEER_NAME="Aakash Khanal"
CMD ["python", "app.py"]