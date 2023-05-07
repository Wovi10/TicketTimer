# TicketTimer
I created this repo to practice my Python and have something I can actually use.
It consists out of two usable script for now:
1. ticketManagement.py
2. clearFile.py

You will need to have Python3 installed for both.
To run any of the scripts, make sure you are located in the 'code' directory of the project.
Both the scripts use a file called List.json. If you do not yet have it, the ticketManagement script will create it for you.

## ticketManagement.py
You can call this script by using following script.
```
python3 ./ticketManagement.py {ticketName}
```
If the given ticket name has not yet been used, a new ticket entry will be created, immediatly setting it to active.
If the given ticket name has already been used and is currently active, it will be put inactive and the time spent will be updated.
If the given ticket name has already been used and is currently inactive, it will be put active.

There will always be at most <ins>one</ins> ticket active.

You can look in the List.json file to see what you have done that day.

### Forgot to clear your file?
Don't worry! All entries that do not have today's date, will be cleared automatically.

## clearFile.py
You can call this script by using following script.
```
python3 ./clearFile.py
```

This will replace the file input with an empty array, ready for new use.

## Possible later additions
A script that prints out all entries in the file in a nice, readable way.

You can always fork this project if you want to add something. Any change requests can be done through issues.
