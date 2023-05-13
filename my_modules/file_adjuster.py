# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from datetime import datetime
import json
from typing import List
from colorama import Fore, Style
from . import FILENAME, WRITE_MODE, DEFAULT_ENCODING, TIME_FORMAT
from .logger import log
from .ticket import Ticket
from .ticket_encoder import TicketEncoder


def override_file(used_tickets: List[Ticket]):
    for ticket in used_tickets:
        ticket.set_defaults()

    with open(FILENAME, WRITE_MODE, encoding=DEFAULT_ENCODING) as file:
        json.dump(used_tickets, file, cls=TicketEncoder)

def stop_busy_tickets(used_tickets: List[Ticket]) -> List[Ticket]:
    new_list = used_tickets
    log(f"{Fore.RED}Stopping{Style.RESET_ALL} tickets:")
    for ticket in new_list:
        log(f"\t- {ticket.name}")
        if not ticket.busy:
            log(f"\t\t{Fore.BLUE}Skipped{Style.RESET_ALL}")
            continue

        minutes_this_session = calculate_total_minutes(ticket)
        ticket.timeWorkedInMinutes += minutes_this_session
        log(f"\t\tWorked {Fore.GREEN}{minutes_this_session}{Style.RESET_ALL} minutes, " +
              f"{Fore.GREEN}{ticket.timeWorkedInMinutes}{Style.RESET_ALL} total")
        ticket.busy = False
        log(f"\t\t{Fore.RED}Stopped{Style.RESET_ALL}")
    log()

    return new_list

def calculate_total_minutes(ticket: Ticket) -> int:
    end_time = datetime.now().strftime(TIME_FORMAT)
    end_time = datetime.strptime(end_time, TIME_FORMAT)
    start_time = datetime.strptime(ticket.startTime, TIME_FORMAT)
    time_difference = end_time - start_time
    return int(time_difference.total_seconds() / 60)


def start_ticket(ticket: Ticket) -> Ticket:
    ticket.startTime = datetime.now().strftime(TIME_FORMAT)
    ticket.busy = True
    log(f"{Fore.GREEN}Started{Style.RESET_ALL} {ticket.name}")
    return ticket
