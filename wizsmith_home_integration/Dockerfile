# Use Home Assistant base image
ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.18
FROM ${BUILD_FROM}

# Set working directory
WORKDIR /app

# Copy add-on files
COPY app /app
COPY run.sh /run.sh
COPY .env.template /data/.env.template

# Install required packages and Python libraries
RUN apk add --no-cache \
    python3 \
    py3-pip \
    ffmpeg \
    espeak \
    jq \
    bash && \
    pip3 install --no-cache-dir \
        paho-mqtt \
        requests \
        python-dotenv

# Ensure permissions and line endings are correct
RUN chmod +x /run.sh && \
    find /app -type f -name "*.py" -exec chmod +x {} \; && \
    dos2unix /run.sh || true

# Environment setup
ENV PYTHONUNBUFFERED=1
ENV LANG C.UTF-8

# Set the default command
CMD ["/run.sh"]
