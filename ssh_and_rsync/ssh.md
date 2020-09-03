# SSH Cheatsheet
### ssh to remote server
```bash
ssh <ip address of remote server>
```
Verbose: you can add as many 'v's as you want behind the ssh flag for verbosity
```bash
ssh -vvvv <ip address of remote server>
```

### SSH tunneling: Forward a specific port
```bash
ssh -N -f -L localhost:<port>:localhost:<port> <username@remote server ip>
```
[tutorial](https://www.youtube.com/watch?v=N8f5zv9UUMI)

### Rsync stuffs
Rsync up
```bash
#! /bin/bash

file=$1
port=$2
echo $file

rsync --progress $file <username@remote ip address>.$port:<remote file directory location>/$file
```


Rsync down
```bash
#! /bin/bash

file=$1
port=$2
echo $file

rsync --progress <username@remote ip address>.$port:<remote file directory location>/$file .
```
