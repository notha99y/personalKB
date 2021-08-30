#! /bin/bash
echo "This works for Ubuntu 16 Proxy version"

http_proxy=$1

sudo systemctl start docker && sudo systemctl enable docker

distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey --proxy "http://$http_proxy" | sudo apt-key add -

curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list --proxy "http://$http_proxy" | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

echo "Installing nvidia-docker-2"
sudo apt-get update
sudo apt-get install -y nvidia-docker2

echo "Installation complete"
echo "Restarting docker"
sudo systemctl restart docker