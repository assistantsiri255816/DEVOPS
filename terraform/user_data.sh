#!/bin/bash
apt-get update -y
apt-get install -y docker.io docker-compose
systemctl start docker
usermod -aG docker ubuntu || true
# Example: pull images from DockerHub (replace with your repo tags)
# docker pull YOUR_DOCKERHUB/python-backend:latest
# docker pull YOUR_DOCKERHUB/python-frontend:latest
# docker pull YOUR_DOCKERHUB/python-logger:latest
# Create a docker-compose.yml on the instance or fetch from S3/Git and run docker-compose up -d
