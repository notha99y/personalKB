#! /bin/bash

echo "This is for Ubuntu 16"

sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

echo "Getting Docker's official GPG key"

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

echo "Verifying Fingerprint"

sudo apt-key fingerprint 0EBFCD88

echo "Installing dockers"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

echo "Docker installed"

echo "Running hello world image"
sudo docker run hello-world