# deep_backup
An single click backup program

This program recreates a single click backup system like iCloud, or similar. This can be done easily with a `cp` command, but for me, who takes local backups quite often, typing it in becomes cumbersome.

## Steps for use:
Look out for the two `"CHANGE ME"` strings. Replace those with the pathnames of your origin and destination folders. Remember to escape characters as required by Python, and the Terminal. I suggest set them to copy your innermost folder you need to backup regularly. To strike a balance between speed and convenience.

Now, running `python3 backup.py` will do a deep copy of your origin path, to your destination path. This is particularly convenient. If however, you want to run it like the normal `cp` command in Unix based systems, with different origin and destination, I have implemented a verbose option. This however, is more like a one-time-setup program, and it will most probably be more convenient to use the `cp` command for that.

## Optional arguments
usage: `backup.py [-h] [-v] [-origin o] [-destination d]`  
Optional arguments:
```
  -h, --help      show this help message and exit
  -v, --verbose   Output files while copying
  
  -origin o       Origin pathname with escape characters.
  -destination d  Destination pathname with escape characters.
```
