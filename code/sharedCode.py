import json
from typing import List
from Constants import FILENAME, WRITE_MODE
from Ticket import Ticket
from TicketEncoder import TicketEncoder


def overWriteFile(usedTickets: List[Ticket]):
    for ticket in usedTickets:
        ticket.setDefaults()
        
    with open(FILENAME, WRITE_MODE) as f:
        json.dump(usedTickets, f, cls=TicketEncoder)