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


# Docker-Compose
## Docker-compose up

## Docker-compose run
The command passed by run overrides the command defined in the service configuration.
For example, if the web service configuration is started with bash, then docker-compose run web python app.py overrides it with python app.py.

The second difference is the docker-compose run command does not create any of the ports specified in the service configuration.
This prevents the port collisions with already open ports. If you do want the service's ports created and mapped to the host, specify the --service-ports flag: