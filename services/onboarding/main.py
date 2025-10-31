import os, json, time, paho.mqtt.client as mqtt, websockets, asyncio

MQTT_HOST = os.getenv("MQTT_HOST", "homeassistant.local")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USER = os.getenv("MQTT_USER", "wizha")
MQTT_PASS = os.getenv("MQTT_PASS", "Pa$$w0rd123")
OR_WS = os.getenv("OR_WS", "wss://74.208.69.198:8443/ws")

async def send_to_openremote(payload):
    try:
        async with websockets.connect(OR_WS) as ws:
            await ws.send(json.dumps(payload))
    except Exception as e:
        print(f"[onboarding] WS error: {e}")

def on_message(client, userdata, msg):
    payload = {"topic": msg.topic, "data": msg.payload.decode()}
    asyncio.run(send_to_openremote(payload))

def main():
    client = mqtt.Client()
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.subscribe("#")
    print("[onboarding] Connected to MQTT. Listening...")
    client.loop_forever()

if __name__ == "__main__":
    main()
