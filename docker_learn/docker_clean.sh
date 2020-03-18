#! /bin/bash
echo "Stopping all docker containers"
docker container stop $(docker container ls -aq)
echo "Removing all docker containers"
docker container rm $(docker container ls -aq)
echo "Finishing up"
docker system prune --volumes