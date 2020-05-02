## ps
Process status, information about processes running in memory.
[more info](https://ss64.com/bash/ps.html)
```bash
ps -ef | grep docker
```
- `-e`: Select all processes, including those of other users.
- `-f`: Full-format listing

## Linux : How to gzip a folder
```bash
tar -cvzf outputfilename foldertocompress
# e.g. tar -cvzf meow.tar.gz meow/
```

## Rename files
```bash
for file in *.png; do mv "$file" "${file/_h.png/_half.png}"; done #  ${string/substring/substitution}
```

## Getting the top levels
```bash
grep -E '^ {2}"' example.json # grabs all first 2 leading spacing things
grep -E '^ {2,6}"' example.json # grabs all the things between 2 and 6 spacings
```
