import os, requests, json

class GeminiVoice:
    def __init__(self, api_key):
        self.api_key = api_key
        # Use the appropriate Gemini endpoint for your organization / key
        self.endpoint = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

    def send_voice_event(self, message):
        if not self.api_key:
            print("[Gemini] No API key configured; skipping send.")
            return
        payload = {"contents": [{"role": "user", "parts": [{"text": message}]}]}
        try:
            r = requests.post(f"{self.endpoint}?key={self.api_key}", json=payload, timeout=10)
            if r.status_code == 200:
                print("[Gemini] Voice event sent successfully.")
            else:
                print("[Gemini] Unexpected status:", r.status_code, r.text)
        except Exception as e:
            print("[Gemini] Error sending voice event:", e)

    def log_sensor_data(self, topic, payload):
        if not self.api_key:
            return
        try:
            # Lightweight logging; consider batching for production
            payload_data = {"topic": topic, "payload": payload}
            r = requests.post(f"{self.endpoint}?key={self.api_key}", json={"contents":[{"role":"user","parts":[{"text":str(payload_data)}]}]}, timeout=10)
            print("[Gemini] Sensor data logged (status):", r.status_code)
        except Exception as e:
            print("[Gemini] Error logging sensor data:", e)
