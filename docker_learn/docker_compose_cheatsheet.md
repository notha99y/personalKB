# Docker-Compose
## Docker-compose up

## Docker-compose run
The command passed by run overrides the command defined in the service configuration.
For example, if the web service configuration is started with bash, then docker-compose run web python app.py overrides it with python app.py.

The second difference is the docker-compose run command does not create any of the ports specified in the service configuration.
This prevents the port collisions with already open ports. If you do want the service's ports created and mapped to the host, specify the --service-ports flag: