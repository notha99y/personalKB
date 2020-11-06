# Changing Docker data directory 
This is for recent version of docker

references:
- https://blog.adriel.co.nz/2018/01/25/change-docker-data-directory-in-debian-jessie/
- https://docs.docker.com/engine/reference/commandline/dockerd/#daemon-configuration-file
- https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169


If you’ve installed Docker with the default settings, it will be storing Docker images, containers and volumes in /var/lib/docker, which will be an issue if you have /var on its own (usually small) partition.

Following are the steps you can take to change the directory even after you created the docker images. 

Note that this requires a restart of docker.

1. Edit `/etc/docker/daemon.json` with the following line
```json
{
    "data-root": "/new/path/to/docker-data"
}
```
2. Stop docker
```bash
sudo systemctl stop docker
```

3. Copy the docker data to the new location
```bash
sudo rsync -axPS /var/lib/docker/ /new/path/to/docker-data
```

4. Start Docker
```bash
sudo systemctl start docker
```

5. Check if Docker is using the new location
```bash
docker info | grep 'Docker Root Dir'
```

6. After ensuring everything is working fine, you can remove the data data
```bash
sudo rm -r /var/lib/docker
```