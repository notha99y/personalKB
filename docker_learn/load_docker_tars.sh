#! /bin/bash
docker_tars=`ls`
for tars in $docker_tars
do
    if [[ "$tar"=*.tar.gz ]]; 
    then
        echo "Loading $tars..."
        zcat $tars | docker load
    fi
done
