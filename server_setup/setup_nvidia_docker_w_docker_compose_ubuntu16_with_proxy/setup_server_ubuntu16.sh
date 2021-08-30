#! /bin/bash

http_proxy=$1

source install_docker.sh $http_proxy

source install_docker_compose.sh $http_proxy

source install_nvidia_docker2.sh $http_proxy