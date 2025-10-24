# WizSmith Home Integration (Home Assistant Add-on v3)

This add-on connects Home Assistant to WizSmith's MQTT and the Gemini API for voice alerts and sensor logging.
It is designed for Raspberry Pi / Home Assistant OS and uses the built-in Mosquitto broker by default.

## Important: Gemini API Key via .env
For security, place your Gemini API key in the add-on's persistent data folder as a `.env` file formatted like:
```
GEMINI_API_KEY=your_real_gemini_key_here
```
You can add this via the Add-on UI (Config -> Show in File Editor) or by placing it in `/config/addons_config/wizsmith_home_integration/.env`.

## Installation
1. Add the GitHub repo to Home Assistant Add-on Store (repository URL).
2. Install the add-on and start it.
3. Add your `.env` with GEMINI_API_KEY.
4. Configure options in the Add-on UI if needed.

## Options (options.json)
- mqtt_host: MQTT broker (default: mqtt://core-mosquitto)
- mqtt_port: MQTT port (default: 1883)
- tts_enabled: Local TTS fallback via espeak if Gemini not available
- gemini_api_env: Environment variable name for GEMINI key (default GEMINI_API_KEY)
- ffmpeg_relay: hls | rtmp | rtsp (camera relay mode)
