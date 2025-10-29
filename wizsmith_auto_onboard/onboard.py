import os
import json
import requests
import paho.mqtt.client as mqtt

# Load HA Add-on options from environment variables
HA_TOKEN = os.environ.get("HA_TOKEN")
MQTT_HOST = os.environ.get("MQTT_HOST")
MQTT_PORT = int(os.environ.get("MQTT_PORT", 1883))
MQTT_USER = os.environ.get("MQTT_USER")
MQTT_PASS = os.environ.get("MQTT_PASS")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
ALERT_EMAIL = os.environ.get("ALERT_EMAIL")
ALERT_PHONE = os.environ.get("ALERT_PHONE")

PI_SERIAL = os.popen("cat /proc/cpuinfo | grep Serial | awk '{print $3}'").read().strip()
HA_URL = "http://homeassistant.local:8123"

# Step 1: Register Pi with central server
print("Registering Pi with central server...")
response = requests.post(
    f"http://{MQTT_HOST}/api/register_pi",
    json={"serial": PI_SERIAL, "capabilities": ["camera", "ai_hat", "sensors"]}
)
business_data = response.json()
BUSINESS_ID = business_data.get("business_id", "default")

# Step 2: Query Home Assistant for sensors and cameras
print("Fetching sensors from Home Assistant...")
headers = {"Authorization": f"Bearer {HA_TOKEN}", "Content-Type": "application/json"}
ha_resp = requests.get(f"{HA_URL}/api/states", headers=headers)
devices = ha_resp.json()

# Step 3: Connect to MQTT broker
print("Connecting to MQTT broker...")
client = mqtt.Client(f"wizsmith_{PI_SERIAL}")
client.username_pw_set(MQTT_USER, MQTT_PASS)
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_start()

# Step 4: Publish all sensors to MQTT
print("Publishing sensors to MQTT...")
for device in devices:
    entity_id = device["entity_id"]
    state = device["state"]
    topic = f"wizsmith/{BUSINESS_ID}/sensors/{entity_id}"
    client.publish(topic, state)

print("WizSmith Add-on started successfully. Pi auto-onboarded and sensors published.")
