import json
from datetime import datetime
from typing import List
from . import TIME_FORMAT, DATE_FORMAT, FILENAME, READ_MODE, Ticket, overWriteFile

def manage(ticketName: str):
    usedTickets: List[Ticket] = getUsedTickets()
    usedTicketNames: List[str] = [ticket.name for ticket in usedTickets] or []
    
    newList = usedTickets
    
    if(isUsedTicket(ticketName, usedTicketNames)):
        newList = handleUsedTicket(ticketName, newList)
    else:
        newList = handleNewTicket(ticketName, newList)
    overWriteFile(newList)


def getUsedTickets() -> List[Ticket]:
    try:
        with open(FILENAME, READ_MODE) as f:
            data = json.load(f)
        usedTickets = [Ticket(**ticket) for ticket in data]
        cleanFile(usedTickets)
        return usedTickets
    except json.JSONDecodeError:
        return []
    
    
def cleanFile(usedTickets: List[Ticket]) -> None:
    newList = []
    for ticket in usedTickets:
        date: str = ticket.date or datetime.now().strftime(DATE_FORMAT)
        if date == datetime.now().strftime(DATE_FORMAT):
            newList.append(ticket)
    overWriteFile(newList)
    

def isUsedTicket(ticketName: str, usedTicketNames: List[str]) -> bool:
    return ticketName in usedTicketNames
    

def handleUsedTicket(ticketName: str, usedTickets: List[Ticket]) -> List[str]:
    newList = usedTickets
    ticketToChange = getTicketToChange(ticketName, newList)
    isBusyTicket = ticketToChange.busy
    newList = stopBusyTickets(newList)
    if not isBusyTicket:
        startTicket(ticketToChange)
    return newList
    

def getTicketToChange(ticketName: str, usedTickets: List[Ticket]) -> Ticket:
    for ticket in usedTickets:
        if ticket.name == ticketName:
            return ticket
    return Ticket()


def stopBusyTickets(usedTickets: List[Ticket]) -> List[Ticket]:
    newList = usedTickets
    for ticket in newList:
        if not ticket.busy:
            continue
        
        endTime = datetime.now().strftime(TIME_FORMAT)
        endTime = datetime.strptime(endTime, TIME_FORMAT)
        startTime = datetime.strptime(ticket.startTime, TIME_FORMAT)
        timeDifference = endTime - startTime
        totalMinutes = int(timeDifference.total_seconds() / 60)
        ticket.timeWorkedInMinutes += totalMinutes
        ticket.busy = False
    return newList
            

def startTicket(ticketToChange: Ticket):
    ticketToChange.startTime = datetime.now().strftime(TIME_FORMAT)
    ticketToChange.busy = True
    
    
def handleNewTicket(name, usedTickets: List[Ticket]) -> List[str]:
    newList = usedTickets
    stopBusyTickets(newList)
    newTicket = Ticket(name)
    newList.append(newTicket)
    
    return newList
