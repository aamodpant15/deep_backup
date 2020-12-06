# deep_backup
An single click backup program

This program recreates a single click backup system like iCloud, or similar. This can be done easily with a `cp` command, but for me, who takes local backups quite often, typing it in becomes cumbersome.

## Steps for use:
Look out for the `"CHANGE ME"` strings. Replace those with the pathnames of your origin and destination folders. Remember to escape characters as required by Python, and the Terminal. I suggest keep them to be your root folder on the origin, and location of your choice on the backup drive.  

Now, running `python3 backup.py` will do a deep copy of your origin path, to your destination path. This is particularly convenient. If however, you want to run it like the normal `cp` command in Unix based systems, I have implemented a verbose option.

## Optional arguments
usage: backup.py [-h] [-v] [-origin o] [-destination d]  
Optional arguments:
```
  -h, --help      show this help message and exit
  -v, --verbose   Output files while copying
  
  -origin o       Origin pathname with escape characters.
  -destination d  Destination pathname with escape characters.
```
