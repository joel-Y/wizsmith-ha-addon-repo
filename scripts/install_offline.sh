#!/bin/bash
set -e
echo "Installing WizSmith Edge Hub (offline mode)"
pip install --no-index --find-links=./wheels -r requirements.txt
