FROM python:3.11-slim

WORKDIR /app
COPY services/ /app/services/
COPY scripts/ /app/scripts/
COPY .env.example /app/.env
RUN apt-get update && apt-get install -y curl && \
    pip install --no-cache-dir paho-mqtt websockets requests

CMD ["python3", "/app/services/onboarding/main.py"]
