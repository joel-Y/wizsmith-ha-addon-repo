#!/usr/bin/env bash
set -e

echo "[WizSmith Edge Hub] Starting all services..."
for svc in onboarding onvif_ws frigate_updater alert_forwarder; do
  echo "Launching $svc..."
  python3 services/$svc/main.py &
done

wait
