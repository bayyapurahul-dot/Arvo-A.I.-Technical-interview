#!/bin/bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl start docker
sudo usermod -aG docker ubuntu

cd /home/ubuntu/hello_flask
docker build -t hello-flask .
docker run -d -p 5000:5000 hello-flask
