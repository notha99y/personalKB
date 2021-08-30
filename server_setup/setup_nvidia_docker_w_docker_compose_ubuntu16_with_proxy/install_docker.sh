#! /bin/bash

echo "This is for Ubuntu 16 Proxy version"
http_proxy=$1

echo 'Acquire::http::Proxy "http://'$http_proxy'";' > /etc/apt/apt.conf

sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

echo "Getting Docker's official GPG key"

curl -fsSL https://download.docker.com/linux/ubuntu/gpg --proxy "http://$http_proxy" | sudo apt-key add -

echo "Verifying Fingerprint"

sudo apt-key fingerprint 0EBFCD88

export http_proxy="http://$http_proxy"

sudo -E add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

echo "Installing dockers"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

echo "Docker installed"