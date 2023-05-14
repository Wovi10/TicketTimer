# TicketTimer
I created this repo to practice my Python and have something I can actually use.
It consists out of two usable script for now:
1. entry.py
2. clear.py

You will need to have Python3 installed for both.
To run any of the scripts, make sure you are located in the root directory of the project (The one that includes /myModules, /resources and the two scripts).
Both the scripts use a file called List.json. If you do not yet have it, the entry script will create it for you.

## entry.py
You can call this script by using following script.
```
python ./entry.py {ticketName}
```
If the given ticket name has not yet been used, a new ticket entry will be created, immediatly setting it to active.
If the given ticket name has already been used and is currently active, it will be put inactive and the time spent will be updated.
If the given ticket name has already been used and is currently inactive, it will be put active.

There will always be at most <ins>one</ins> ticket active.

You can look in the List.json file to see what you have done that day.

### Forgot to clear your file?
Don't worry! All entries that do not have today's date, will be cleared automatically.

## clear.py
You can call this script by using following script.
```
python ./clear.py
```
This will replace the file input with an empty array, ready for new use.

## rename.py
You can call this script by using following script.
```
python ./rename.py {oldTicketName} {newTicketName}
```
This script will update the old ticketname to the new ticketname if it exists.
If it doesn't exist, you will receive an error in the console and the script will stop.

## update_entry.py
You can call this script by using following script.
```
python ./update_entry.py {ticketName}
```
If the given ticket is not in you list.json file, you will receive an error in the  console and the program will not do anything.  
If the script is in the list.json file, the ticket startTime and timeWorkedInMinutes will be updated.

## Extra functionalities
I have added a Logger file to make printing even easier. Feel free to implement extra things to it.

## Possible later additions
Things that might be added are visible in the Issues.  
You can always fork this project if you want to add something. Any change requests can be done through issues.