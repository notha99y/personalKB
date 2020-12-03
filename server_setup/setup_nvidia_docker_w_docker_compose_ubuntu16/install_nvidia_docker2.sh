#! /bin/bash
echo "This works for Ubuntu 16"

curl https://get.docker.com | sh

sudo systemctl start docker && sudo systemctl enable docker

distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

echo "Installing nvidia-docker-2"
sudo apt-get update
sudo apt-get install -y nvidia-docker2

echo "Installation complete"
echo "Restarting docker"
sudo systemctl restart docker

echo "Testing installation"
sudo docker run --rm --gpus all nvidia/cuda:9.0-base nvidia-smi