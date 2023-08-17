# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import json
import sys

from my_modules.ticket_encoder import TicketEncoder

from . import FILENAME, WRITE_MODE, DEFAULT_ENCODING
from .logger import error

def clear():
    with open(FILENAME, WRITE_MODE, encoding=DEFAULT_ENCODING) as file:
        json.dump('', file, cls=TicketEncoder)
    error("File cleared")
    sys.exit(0)
