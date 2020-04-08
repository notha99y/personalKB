# Docker Cheatsheet

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
- Error
```bash
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?`
```
- Solution
```bash
sudo service docker start
```