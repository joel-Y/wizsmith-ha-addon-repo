FROM python:3.12-slim

# Install dependencies
RUN pip install --no-cache-dir paho-mqtt requests websocket-client

# Copy add-on files
COPY onboard.py /app/onboard.py
COPY frigate.yml /app/frigate.yml
COPY run.sh /app/run.sh
COPY requirements.txt /app/requirements.txt

WORKDIR /app

# Make run script executable
RUN chmod +x run.sh

CMD ["./run.sh"]
