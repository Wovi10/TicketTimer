from datetime import datetime
import json
from typing import List

TIMEFORMAT = '%H:%M'


def main():
    while(True):
        usedTicketNames: List[str] = getUsedTicketNames()
        ticketName = askTicketName()
        checkValue(ticketName)
        if(checkIsUsedTicket(ticketName, usedTicketNames)):
            handleUsedTicket(ticketName, usedTickets) 
        else:
            handleNewTicket(ticketName, usedTickets)
        overWriteFile(usedTickets)


def getUsedTicketNames():
    usedTickets = getUsedTickets()
    return [ticket["name"] for ticket in usedTickets]
    

def getUsedTickets():
    with open('.\list.json', 'r') as f:
        data = json.load(f)
    return list(map(lambda ticket: ticket, data))


def askTicketName():
    return input("Ticket name('end' to stop):")
    

def checkValue(ticketName: str):
    if(ticketName == 'end'): 
        quit(0)


def checkIsUsedTicket(ticketName: str, usedTicketNames):
    if(usedTicketNames.__contains__(ticketName)):
        return True
    return False
    

def handleUsedTicket(ticketName: str, usedTickets):
    ticketToChange = getTicketToChange(ticketName, usedTickets)
    isBusyTicket: bool = ticketToChange['busy']
    stopBusyTickets(usedTickets)
    if not isBusyTicket:
        usedTickets = startTicket(ticketToChange)
    

def getTicketToChange(ticketName: str, usedTickets):
    for ticket in usedTickets:
        if ticket['name'] == ticketName:
            return ticket


def stopBusyTickets(usedTickets):
    for ticket in usedTickets:
        if not ticket['busy']:
            break
        
        endTime = datetime.now().strftime(TIMEFORMAT)
        endTime = datetime.strptime(endTime, TIMEFORMAT)
        startTime = datetime.strptime(ticket['startTime'], TIMEFORMAT)
        timeDifference = endTime - startTime
        totalMinutes = int(timeDifference.total_seconds() / 60)
        if ticket['timeWorkedInMinutes'] != "":
            totalMinutes += int(ticket['timeWorkedInMinutes'])
        ticket['timeWorkedInMinutes'] = totalMinutes
        ticket['busy'] = False
            

def startTicket(ticketToChange):
    ticketToChange['startTime'] = datetime.now().strftime(TIMEFORMAT)
    ticketToChange['busy'] = True


def overWriteFile(usedTickets):
     with open('.\list.json', 'w') as f:
        json.dump(usedTickets, f)
    
    
def handleNewTicket(ticketName, usedTickets: List[any]):
    stopBusyTickets(usedTickets)
    newTicket = {
        "name": ticketName,
        "busy": True,
        "startTime": datetime.now().strftime(TIMEFORMAT),
        "timeWorkedInMinutes": ""
    }
    usedTickets.append(newTicket)
    
    
if __name__ == "__main__":
    main()