# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import json
from typing import List
from . import FILENAME, WRITE_MODE, DEFAULT_ENCODING
from .ticket import Ticket
from .ticket_encoder import TicketEncoder


def override_file(used_tickets: List[Ticket]):
    for ticket in used_tickets:
        ticket.set_defaults()

    with open(FILENAME, WRITE_MODE, encoding=DEFAULT_ENCODING) as file:
        json.dump(used_tickets, file, cls=TicketEncoder)
