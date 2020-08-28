# SSH Cheatsheet
### ssh to remote server
```bash
ssh <ip address of remote server>
```
Verbose: you can add as many 'v's as you want behind the ssh flag for verbosity
```bash
ssh -vvvv <ip address of remote server>
```

### Rsync stuffs
Rsync up
```bash
#! /bin/bash

file=$1
port=$2
echo $file

rsync --progress $file <remote ip address>.$port:<remote file directory location>/$file
```


Rsync down
```bash
#! /bin/bash

file=$1
port=$2
echo $file

rsync --progress <remote ip address>.$port:<remote file directory location>/$file .
```
