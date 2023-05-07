from json import JSONEncoder
from . import Ticket


class TicketEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Ticket):
            return obj.__dict__
        return super().default(obj)