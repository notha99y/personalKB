# Nvidia docker Images
Main repo [tags](https://hub.docker.com/r/nvidia/cuda/tags)
- choose those with `cudnn-devel`

## Nvidia GPU Cloud (NGC)
- [useful link](https://www.pugetsystems.com/labs/hpc/How-To-Setup-NVIDIA-Docker-and-NGC-Registry-on-your-Workstation---Part-4-Accessing-the-NGC-Registry-1115/)
### NGC Docker Registry
The registry domain name is `nvcr.io` a.k.a. Nvidia Container Registry
1. Login to the NGC registry from docker before to access the container images

[tags](https://ngc.nvidia.com/catalog/containers/nvidia:cuda/tags)

Seems to me that actually the tag they used are the same. Just the domain name is different. e.g.

```docker
FROM nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04
FROM nvcr.io/nvidia/cuda:9.2-cudnn7-devel-ubuntu16.04
```