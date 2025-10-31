#!/usr/bin/env bash
set -e
echo "Installing Python wheels offline..."
pip install --no-index --find-links=./wheels -r requirements.txt || echo "Done"
