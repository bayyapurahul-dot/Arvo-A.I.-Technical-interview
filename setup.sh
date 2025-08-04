#!/bin/bash
set -e
sudo apt-get update -y
sudo apt-get install -y python3-pip
pip3 install flask
# Kill any previous python app running on port 5000 (optional cleanup)
fuser -k 5000/tcp || true
# Start the Flask app in background and redirect output to a log file
nohup python3 /home/azureuser/app.py > flask.log 2>&1 &
