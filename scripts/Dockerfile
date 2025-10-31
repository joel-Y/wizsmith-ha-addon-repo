FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt ./
COPY services ./services
COPY run.sh .
COPY .env.example .env
RUN chmod +x run.sh

# Offline wheel install if available
COPY wheels ./wheels
RUN if [ -d "./wheels" ] && [ "$(ls -A wheels)" ]; then \
    pip install --no-index --find-links=./wheels -r requirements.txt; \
    else pip install -r requirements.txt; fi

CMD ["./run.sh"]
