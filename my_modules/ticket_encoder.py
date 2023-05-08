from json import JSONEncoder
from . import Ticket


class TicketEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Ticket):
            return o.__dict__
        return super().default(o)
