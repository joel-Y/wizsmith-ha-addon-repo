import os, time, paho.mqtt.client as mqtt
import json, websocket

mqtt_host = os.getenv("MQTT_HOST", "localhost")
mqtt_port = int(os.getenv("MQTT_PORT", "1883"))
mqtt_user = os.getenv("MQTT_USER", "")
mqtt_pass = os.getenv("MQTT_PASS", "")
ws_url = os.getenv("OPENREMOTE_WS", "wss://74.208.69.198:8443/ws")

print("🔗 Connecting to MQTT:", mqtt_host)
client = mqtt.Client()
client.username_pw_set(mqtt_user, mqtt_pass)
client.connect(mqtt_host, mqtt_port, 60)

print("🌐 Connecting to OpenRemote WS:", ws_url)
ws = websocket.create_connection(ws_url, timeout=10)

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        ws.send(json.dumps({"topic": msg.topic, "payload": payload}))
        print(f"📡 Forwarded {msg.topic}")
    except Exception as e:
        print("Error:", e)

client.on_message = on_message
client.subscribe("#")

print("✅ Bridge running...")
client.loop_forever()
