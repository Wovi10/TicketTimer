# TicketTimer
The script ```tickettimer.py``` can be used to run all scripts.
call it as follows:
```
python ./tickettimer.py function "Possible Arguments"
```

I created this repo to practice my Python and have something I can actually use.
It consists out of following usable funcitons:
1. entry
2. print_tickets
3. delete
4. clear
5. mock_data
6. rename
7. stop
8. time_worked
9. update

You will need to have Python3 installed for both.
To run any of the scripts, make sure you are located in the root directory of the project (The one that includes /myModules, /resources and the two scripts).
Both the scripts use a file called list.json. If you do not yet have it, the entry script will create it for you.

## entry
You can call this function by using following command:
```
python ./tickettimer.py entry "Ticket name"
```
If the given ticket name has not yet been used, a new ticket entry will be created, immediately setting it to active.
If the given ticket name has already been used and is currently active, it will be put inactive and the time spent will be updated.
If the given ticket name has already been used and is currently inactive, it will be put active.

There will always be at most <ins>one</ins> ticket active.

### Forgot to clear your file?
Don't worry! All entries that do not have today's date, will be cleared automatically.

## print_tickets
You can call this function by using following command:
```
python ./tickettimer.py print_tickets
```
Will list all tickets of today, including  their time worked in minutes and if they are currently active or not.

## delete
You can call this function by using following command:
```
python ./tickettimer.py delete "Ticket name"
```
This will delete the entry from the list.

## clear
You can call this function by using following command:
```
python ./tickettimer.py clear
```
This will replace the file input with an empty array, ready for new use.

## mock_data
You can call this function by using following command:
```
python ./tickettimer.py mock_data
```
This will create a list with mock data to test on.

## rename
You can call this function by using following command:
```
python ./tickettimer.py rename "old ticket" "new ticket"
```
This will update the old ticketname to the new ticketname if it exists.
If it doesn't exist, you will receive an error in the console and the script will stop.

## stop
You can call this function by using following command:
```
python ./tickettimer.py stop
```
This will stop any running ticket.

## time_worked
You can call this function by using following command:
```
python ./tickettimer.py time_worked
```
This will print the total time worked (in minutes) to your console.

## update
You can call this function by using following command:
```
python ./tickettimer.py update
```
This will update the currently active ticket startTime and timeWorkedInMinutes.
If a ticket is not active, it will be skipped.

## Extra functionalities
I have added a Logger file to make printing even easier. Feel free to implement extra things to it.

## Possible later additions
Things that might be added are visible in the Issues.  
You can always fork this project if you want to add something.  
Any change requests can be done through issues.