# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from datetime import datetime
from colorama import Fore, Style
from .logger import log
from . import TIME_FORMAT, DATE_FORMAT


class Ticket:
    NAME_DEFAULT = ""
    BUSY_DEFAULT = False
    STARTTIME_DEFAULT = datetime.now().strftime(TIME_FORMAT)
    TIMEWORKED_DEFAULT = 0
    DATE_DEFAULT = datetime.now().strftime(DATE_FORMAT)

    # pylint: disable=invalid-name
    # pylint: disable=too-many-arguments
    def __init__(self, name=NAME_DEFAULT, busy=BUSY_DEFAULT, startTime=STARTTIME_DEFAULT,
                 timeWorkedInMinutes=TIMEWORKED_DEFAULT, date=DATE_DEFAULT):
        self.name = name
        self.busy = busy
        self.startTime = startTime
        self.timeWorkedInMinutes = timeWorkedInMinutes
        self.date = date


    def set_defaults(self):
        self.name = self.name or Ticket.NAME_DEFAULT
        self.busy = self.busy or Ticket.BUSY_DEFAULT
        self.startTime = self.startTime or Ticket.STARTTIME_DEFAULT
        self.timeWorkedInMinutes = self.timeWorkedInMinutes or Ticket.TIMEWORKED_DEFAULT
        self.date = self.date or Ticket.DATE_DEFAULT


    def to_string(self):
        if self.busy:
            busy_text = f"{Fore.GREEN}Busy.{Style.RESET_ALL}"
        else:
            busy_text = f"{Fore.RED}Not busy.{Style.RESET_ALL}"
        log(f"- {Fore.BLUE}{self.name}{Style.RESET_ALL}: Worked for " \
            f"{self.timeWorkedInMinutes} minutes. {busy_text}")
