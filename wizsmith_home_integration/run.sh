#!/usr/bin/env bash
set -e
echo "Starting WizSmith Home Integration add-on..."

# Load HA add-on options
if [ -f /data/options.json ]; then
  MQTT_HOST=$(jq -r '.mqtt_host' /data/options.json)
  MQTT_PORT=$(jq -r '.mqtt_port' /data/options.json)
  TTS_ENABLED=$(jq -r '.tts_enabled' /data/options.json)
  GEMINI_ENV_NAME=$(jq -r '.gemini_api_env' /data/options.json)
  FFMPEG_RELAY=$(jq -r '.ffmpeg_relay' /data/options.json)
else
  echo "No /data/options.json found; using defaults"
  MQTT_HOST="mqtt://core-mosquitto"
  MQTT_PORT=1883
  TTS_ENABLED=true
  GEMINI_ENV_NAME="GEMINI_API_KEY"
  FFMPEG_RELAY="hls"
fi

# Load .env if present in /data (persisted by user in Add-on UI or supervisor)
if [ -f /data/.env ]; then
  export $(cat /data/.env | xargs)
else
  echo "Warning: /data/.env not found. Create it and add your GEMINI_API_KEY as $GEMINI_ENV_NAME for Gemini features."
fi

# Export variables for Python app
export MQTT_HOST="${MQTT_HOST}"
export MQTT_PORT="${MQTT_PORT}"
export TTS_ENABLED="${TTS_ENABLED}"
export FFMPEG_RELAY="${FFMPEG_RELAY}"

# GEMINI key is expected to be in environment as the name specified by gemini_api_env
if [ -n "${GEMINI_ENV_NAME}" ]; then
  GEMINI_KEY=$(printenv "${GEMINI_ENV_NAME}")
  export GEMINI_API_KEY="${GEMINI_KEY}"
fi

echo "MQTT host: $MQTT_HOST"
echo "TTS enabled: $TTS_ENABLED"
echo "FFmpeg relay mode: $FFMPEG_RELAY"
if [ -n "$GEMINI_API_KEY" ]; then
  echo "Gemini API key present in environment."
else
  echo "Gemini API key NOT found. Gemini features will be disabled until you place a .env in Supervisor Add-on store or /config/addons_config/wizsmith_home_integration/ with GEMINI_API_KEY."
fi

# Start the main Python app
python3 /app/main.py
