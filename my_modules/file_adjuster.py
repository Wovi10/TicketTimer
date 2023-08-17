# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from datetime import datetime
import json
from pathlib import Path
from typing import List
from colorama import Fore, Style
from . import FILENAME, WRITE_MODE, DEFAULT_ENCODING, TIME_FORMAT, READ_MODE, DATE_FORMAT
from .logger import log, error
from .ticket import Ticket
from .ticket_encoder import TicketEncoder


def override_file(used_tickets: List[Ticket]):
    try:
        ticket_arrays = []
        if Path(FILENAME).is_file():
            with open(FILENAME, READ_MODE, encoding=DEFAULT_ENCODING) as file:
                data = json.load(file)
            if not data == '':
                first_item: Ticket = data[0][0]
                date: str = first_item['date'] or datetime.now().strftime(DATE_FORMAT)
                
                if date != datetime.now().strftime(DATE_FORMAT):
                    in_file: List[Ticket] = [Ticket(**ticket) for ticket in data[0]]
                    ticket_arrays.insert(0, in_file)
                elif len(data) > 1:
                    in_file: List[Ticket] = [Ticket(**ticket) for ticket in data[1]]

        ticket_arrays.insert(0, used_tickets)

        with open(FILENAME, WRITE_MODE, encoding=DEFAULT_ENCODING) as file:
            json.dump(ticket_arrays, file, cls=TicketEncoder)
        log("Done overriding file")
        return
    except json.JSONDecodeError as err:
        error(err.msg)
        return


def stop_busy_tickets(used_tickets: List[Ticket]) -> List[Ticket]:
    new_list = used_tickets
    if len(new_list) > 0:
        log(f"{Fore.RED}Stopping{Style.RESET_ALL} tickets:")
        for ticket in new_list:
            if not ticket.busy:
                continue
            log(f"\t- {ticket.name}")

            ticket = update_total_minutes_worked(ticket)
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


def update_total_minutes_worked(ticket: Ticket) -> Ticket:
    minutes_this_session = calculate_total_minutes(ticket)
    ticket.timeWorkedInMinutes += minutes_this_session
    ticket.startTime = datetime.now().strftime(TIME_FORMAT)
    log(f"\t\tWorked {Fore.GREEN}{minutes_this_session}{Style.RESET_ALL} minutes, " +
        f"{Fore.GREEN}{ticket.timeWorkedInMinutes}{Style.RESET_ALL} total")
    return ticket


def start_ticket(ticket: Ticket) -> Ticket:
    ticket.startTime = datetime.now().strftime(TIME_FORMAT)
    ticket.busy = True
    log(f"{Fore.GREEN}Started{Style.RESET_ALL} {ticket.name}")
    return ticket


def stop_ticket(ticket: Ticket) -> Ticket:
    ticket = update_total_minutes_worked(ticket)
    ticket.busy = False
    log(f"{Fore.RED}Stopped{Style.RESET_ALL} {ticket.name}")
    return ticket
