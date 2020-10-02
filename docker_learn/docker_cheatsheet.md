# Docker Cheatsheet
## Storage location of Docker Containers and Images
[source](https://www.freecodecamp.org/news/where-are-docker-images-stored-docker-container-paths-explained/)

A Docker container consists of `network settings`, `volumes`, and `images`. The location of Docker files depends on your operating system. Here is an overview for the most used operating systems:
- Ubuntu: /var/lib/docker/
- Fedora: /var/lib/docker/
- Debian: /var/lib/docker/
- Windows: C:\ProgramData\DockerDesktop
- MacOS: ~/Library/Containers/com.docker.docker/Data/vms/0/

Inside `/var/lib/docker`, different information is stored. For example, data for containers, volumes, builds, networks, and clusters.

The heaviest contents are usually images and the default storage driver overlay2 will store them in `/var/lib/docker/overlay2`
## Docker Image
- See list of docker images
```bash
docker images
```
- Build image from Dockerfile
```bash
docker build -t <image name> <dockerfile folder path>
# image name: notha99y/pytesseract:1.1
```
- Rename existing image
```bash
docker tag <old image name/id> <new image name/id>
```
- Remove existing image
```bash
docker rmi <image name/id>
```
- Save existing image
```bash
docker save -o <path for generated tar file> <image name/id>
```

```bash
docker save <image name/id> | gzip > <path for generated tar file> 
# docker save notha99y/pytesseract:1.1 | gzip > pytesseract.tar.gz 
```
- Loading a .tar file
```bash
docker load -i <path to tar file>
``` 
- Loading a .tar.gz file
```bash
zcat file.tar.gz | docker load
```

## Docker Container
- See list of docker containers
```bash
docker container ls -a
```
- SSH into running container
```bash
docker exec -it <container name> /bin/bash
```
- stop docker containers
```bash
docker container stop <container id>
docker container stop $(docker container ls -aq) # stop all containers 
```
- remove docker containers (ensure they are stopped first)
```bash
docker container rm <container id>
docker container rm $(docker container ls -aq) # removes all stopped containers
```
- checking docker logs
```bash
docker logs -f <container name>
```
- List the volumes
```bash
docker volume ls
```
- Check that the volumes was created
```bash
docker volume inspect <volume name>
```

## Remove all usused objects
- Removes all stopped containers, all dangling images and all unused networks:
```bash
docker system prune
```
- remove all unused volumes
```bash
docker system prune --volumes
```

## Docker run
- run with GUI (not tested with jupyter notebook)
```
docker run -it -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix  <image name>
```

## Common bugs
### Error 1: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
- Solution
```bash
sudo service docker start
```

### Error 2:Couldn’t connect to Docker daemon at http+docker://localhost – is it running?
reference: https://techoverflow.net/2019/03/16/how-to-fix-error-couldnt-connect-to-docker-daemon-at-httpdocker-localhost-is-it-running/
- Solution

Two possible reasons for this error message

1. The user you are running the command as does not have the permissions to access docker. 

You can fix this by either running as super user `sudo` or adding your user to the `docker` group with the following command
```bash
sudo usernod -a -G docker $USER
```
You would have to log out and login back for this to take effect

2. You have not started docker
```bash
sudo systemctl start docker
```
