import os, time
from mqtt_handler import WizSmithMQTT
from gemini_client import GeminiVoice

MQTT_HOST = os.getenv("MQTT_HOST", "core-mosquitto").replace("mqtt://", "")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
TTS_ENABLED = os.getenv("TTS_ENABLED", "true").lower() == "true"

gemini = GeminiVoice(GEMINI_API_KEY) if GEMINI_API_KEY else None
mqtt_client = WizSmithMQTT(MQTT_HOST, MQTT_PORT, gemini, tts_enabled=TTS_ENABLED)

mqtt_client.connect()
mqtt_client.subscribe("homeassistant/sensor/#")
mqtt_client.subscribe("homeassistant/state/#")
mqtt_client.subscribe("wizsmith/alerts/#")

print("[WizSmith] Listening for MQTT topics...")

try:
    while True:
        mqtt_client.loop()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Shutting down...")
