#! /bin/bash
echo "Fetch keys"
sudo apt-key adv --fetch-keys  http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo bash -c 'echo "deb http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/cuda.list'

sudo apt update

echo "Installing Cuda and Nvidia Driver"
sudo apt -y install cuda