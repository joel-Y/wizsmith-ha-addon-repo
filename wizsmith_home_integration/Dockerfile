ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.18
FROM ${BUILD_FROM}

WORKDIR /app

# Copy files
COPY app /app
COPY run.sh /run.sh
COPY .env.template /data/.env.template

# Install system dependencies and create Python venv
RUN apk add --no-cache python3 py3-pip ffmpeg espeak jq bash \
 && python3 -m venv /venv \
 && . /venv/bin/activate \
 && pip install --no-cache-dir paho-mqtt requests python-dotenv

# Ensure scripts use the venv Python
ENV PATH="/venv/bin:$PATH"

CMD ["/run.sh"]
