# Run Chronic Tasks
## About
On Unix-like OS, the crontab command opens the cron table for editing. The cron table is the list of tasks scheduled to run at regular time intervals on the system.

The daemon which reads the crontab and executres the commands at the right time is called cron. It's named after Kronos, the Greek god of time.

You can check all the crontabs written here 
```bash
/var/spool/cron/crontabs
```

## Syntax
```bash
crontab [-u user] file
```

```bash
crontab [-u user] [-l | -r | -e] [-i] [-s]
```
### Options
- -u user: specifies the user whose `crontab` is to be viewed or modified
- -l: display the current crontab
- -r: remove the current crontab
- -e: Edit the current crontab, using the editor specified
- -i: Same as `-r`, but gives the user a yes/no confirmation prompt before removeing the crontab
- -s: SELinux only: appends the current SELinux security conext string as an MLS_LEVEL

## Crontab entries examples
- Run the shell script /home/renjie/backup.sh on Jan 2 at 6:15 am
```bash
15 6 2 1 * /home/renjie/backup.sh
```

- Run script at 10:30pm every weekday:
```bash
30 22 * * Mon,Tue,Wed,Thu,Fri /home/renjie/backup.sh
```

- Run script at 9am everyday:
```bash
0 9 * * * /home/renjie/backup.sh
```

## Reference
- https://www.computerhope.com/unix/ucrontab.htm