#!/bin/bash
set -e
echo "Building offline .whl packages..."
mkdir -p wheels
pip download -r requirements.txt -d wheels/
echo "Wheel packages have been built and stored in the 'wheels' directory."