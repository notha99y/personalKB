#! /bin/bash
echo "This is for Ubuntu 16 Proxy version"

http_proxy=$1

sudo curl --proxy "http://$http_proxy" -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "Docker-compose installation complete"
sudo docker-compose --version