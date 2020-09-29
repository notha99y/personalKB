# Docker-Compose
## Specifying a host path for a container volume
With the `local` volume driver comes the ability to use arbitrary mounts. By using [bind mount](https://docs.docker.com/storage/bind-mounts/) you can achieve this. [Solution source](https://stackoverflow.com/questions/36387032/how-to-set-a-path-on-host-for-a-named-volume-in-docker-compose-yml)
```yaml
verison: '2' 
# works for 3 also
services:
  db:
    image: mysql
    volumes:
      - dbdata:/var/lib/mysql
volumes:
  dbdata:
    driver: local
    driver_opts:
      type: 'none'
      o: 'bind'
      device: '/srv/db-data'
```

## Docker-compose up
Run in detached mode
```bash
docker-compose up -d 
```
## Docker-compose run
The command passed by run overrides the command defined in the service configuration.
For example, if the web service configuration is started with bash, then docker-compose run web python app.py overrides it with python app.py.

The second difference is the docker-compose run command does not create any of the ports specified in the service configuration.
This prevents the port collisions with already open ports. If you do want the service's ports created and mapped to the host, specify the --service-ports flag:

## Fixing runtime nvidia
As of 9 May 2020, the new docker-compose does not support the nvidia runtime. The --gpu all flag does not work.
A work around can be found [here](https://github.com/NVIDIA/nvidia-container-runtime#docker-engine-setup)

