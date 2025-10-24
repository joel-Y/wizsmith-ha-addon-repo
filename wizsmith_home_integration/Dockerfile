ARG BUILD_FROM=ghcr.io/home-assistant/amd64-base:3.18
FROM ${BUILD_FROM}

WORKDIR /app
COPY app /app
COPY run.sh /run.sh
COPY .env.template /data/.env.template

RUN apk add --no-cache python3 py3-pip ffmpeg espeak jq bash \
 && pip3 install paho-mqtt requests python-dotenv

CMD ["/run.sh"]
