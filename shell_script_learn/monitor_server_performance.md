# Useful bash commands to monitor server performance
## GPU 
```bash
watch nvidia-smi
```

## CPU
```bash
htop
htop -p PID,PID,PID # to filter by PIDs
```

## Docekr
### Container status
```bash
watch docker ps
```
### Container logs
When running in `detached` mode, you can pick into the the logs of the container via
```bash
docker logs <container name> -f
```