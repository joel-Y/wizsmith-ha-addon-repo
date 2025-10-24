import paho.mqtt.client as mqtt
import json, os, subprocess

class WizSmithMQTT:
    def __init__(self, host, port, gemini, tts_enabled=True):
        self.host = host
        self.port = port
        self.gemini = gemini
        self.tts_enabled = tts_enabled
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self):
        self.client.connect(self.host, self.port, 60)
        self.client.loop_start()

    def subscribe(self, topic):
        self.client.subscribe(topic)
        print(f"[WizSmith] Subscribed to {topic}")

    def loop(self):
        # loop is handled by loop_start; small sleep here for cooperative scheduling
        pass

    def on_connect(self, client, userdata, flags, rc):
        print(f"[WizSmith] MQTT connected with code: {rc}")

    def on_message(self, client, userdata, msg):
        topic = msg.topic
        payload = msg.payload.decode('utf-8', errors='ignore')
        print(f"[MQTT] {topic} -> {payload}")
        # Alerts -> Gemini voice event or TTS
        if topic.startswith("wizsmith/alerts"):
            if self.gemini:
                try:
                    self.gemini.send_voice_event(payload)
                except Exception as e:
                    print("[WizSmith] Gemini send failed:", e)
            elif self.tts_enabled:
                try:
                    subprocess.run(["espeak", payload], check=False)
                except Exception as e:
                    print("[WizSmith] Local TTS failed:", e)
        # Sensor updates -> log to Gemini if available
        if topic.startswith("homeassistant/sensor") and self.gemini:
            try:
                self.gemini.log_sensor_data(topic, payload)
            except Exception as e:
                print("[WizSmith] Gemini log failed:", e)
