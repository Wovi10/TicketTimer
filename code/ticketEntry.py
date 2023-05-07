from datetime import datetime
import json
import sys
from typing import List

ALL_FIELDS = [
    (NAME_FIELD, ""), 
    (BUSY_FIELD, False), 
    (STARTTIME_FIELD, datetime.now().strftime(TIME_FORMAT)),
    (TIMEWORKED_FIELD, 0),
    (DATE_FIELD, datetime.now().strftime(DATE_FORMAT))
    ]


def main(ticketName: str):
    usedTickets = getUsedTickets()
    cleanFile(usedTickets)
    usedTicketNames: List[str] = [ticket[NAME_FIELD] for ticket in usedTickets]
    
    if(isUsedTicket(ticketName, usedTicketNames)):
        handleUsedTicket(ticketName, usedTickets)
    else:
        handleNewTicket(ticketName, usedTickets)
    overWriteFile(usedTickets)
    

def getUsedTickets():
    try:
        with open(FILENAME, READ_MODE) as f:
            data = json.load(f)
        return list(lambda ticket: ticket, data)
    except json.JSONDecodeError:
        return []
    
    
def cleanFile(usedTickets: List[any]):
    newList = []
    for ticket in usedTickets:
        date: str = ticket.get(DATE_FIELD, None)
        if date == datetime.now().strftime(DATE_FORMAT):
            newList.append(ticket)
    usedTickets = newList
    overWriteFile(usedTickets)
    

def isUsedTicket(ticketName: str, usedTicketNames: List[str]):
    return ticketName in usedTicketNames
    

def handleUsedTicket(ticketName: str, usedTickets: List[any]):
    ticketToChange = getTicketToChange(ticketName, usedTickets)
    isBusyTicket: bool = ticketToChange[BUSY_FIELD]
    stopBusyTickets(usedTickets)
    if not isBusyTicket:
        startTicket(ticketToChange)
    

def getTicketToChange(ticketName: str, usedTickets: List[any]):
    for ticket in usedTickets:
        if ticket[NAME_FIELD] == ticketName:
            return ticket


def stopBusyTickets(usedTickets: List[any]):
    for ticket in usedTickets:
        if not ticket[BUSY_FIELD]:
            break
        
        endTime = datetime.now().strftime(TIME_FORMAT)
        endTime = datetime.strptime(endTime, TIME_FORMAT)
        startTime = datetime.strptime(ticket[STARTTIME_FIELD], TIME_FORMAT)
        timeDifference = endTime - startTime
        totalMinutes = int(timeDifference.total_seconds() / 60)
        if ticket[TIMEWORKED_FIELD] != 0:
            totalMinutes += int(ticket[TIMEWORKED_FIELD])
        ticket[TIMEWORKED_FIELD] = totalMinutes
        ticket[BUSY_FIELD] = False
            

def startTicket(ticketToChange):
    ticketToChange[STARTTIME_FIELD] = datetime.now().strftime(TIME_FORMAT)
    ticketToChange[BUSY_FIELD] = True
    
    
def handleNewTicket(ticketName, usedTickets: List[any]):
    stopBusyTickets(usedTickets)
    newTicket = {
        NAME_FIELD: ticketName,
        BUSY_FIELD: True,
        STARTTIME_FIELD: datetime.now().strftime(TIME_FORMAT),
        TIMEWORKED_FIELD: 0,
        DATE_FIELD: datetime.now().strftime(DATE_FORMAT)
    }
    usedTickets.append(newTicket)
    
    
def overWriteFile(usedTickets):
    for ticket in usedTickets:
        for key, value in ALL_FIELDS:
            ticket[key] = ticket.get(key, value)
        
    with open(FILENAME, WRITE_MODE) as f:
        json.dump(usedTickets, f)
    


class Constants:
    FILENAME = '.\list.json'
    READ_MODE = 'r'
    WRITE_MODE = 'w'
    TIME_FORMAT = '%H:%M'
    DATE_FORMAT = '%Y-%m-%d'
    NAME_FIELD = 'name'
    DATE_FIELD = 'date'
    BUSY_FIELD = 'busy'
    STARTTIME_FIELD = 'startTime'
    TIMEWORKED_FIELD = 'timeWorkedInMinutes'



 
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: A ticketName is required.")
        sys.exit(1)
    param = sys.argv[1]
    main(param)