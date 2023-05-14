# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import json
from datetime import datetime
from typing import List
from colorama import Fore, Style

from . import DATE_FORMAT, FILENAME, READ_MODE, DEFAULT_ENCODING
from .logger import log, error
from .ticket import Ticket
from .file_adjuster import (override_file, stop_busy_tickets, 
                            start_ticket, update_total_minutes_worked)


def add_entry(ticket_name: str) -> None:
    used_tickets: List[Ticket] = get_used_tickets()
    used_ticket_names: List[str] = [ticket.name for ticket in used_tickets] or []

    new_list = used_tickets

    if ticket_name in used_ticket_names:
        new_list = handle_used_ticket(ticket_name, new_list)
    else:
        new_list = handle_new_ticket(ticket_name, new_list)
    override_file(new_list)
    return


def get_used_tickets() -> List[Ticket]:
    try:
        with open(FILENAME, READ_MODE, encoding=DEFAULT_ENCODING) as file:
            data = json.load(file)
        used_tickets = [Ticket(**ticket) for ticket in data]
        clean_file(used_tickets)
        return used_tickets
    except json.JSONDecodeError:
        return []


def clean_file(used_tickets: List[Ticket]) -> None:
    new_list = []
    for ticket in used_tickets:
        date: str = ticket.date or datetime.now().strftime(DATE_FORMAT)
        if date == datetime.now().strftime(DATE_FORMAT):
            new_list.append(ticket)
    override_file(new_list)


def handle_used_ticket(ticket_name: str, used_tickets: List[Ticket]) -> List[str]:
    new_list = used_tickets
    ticket_to_change = get_ticket_to_change(ticket_name, new_list)
    is_busy_ticket = ticket_to_change.busy
    if len(new_list) > 0:
        new_list = stop_busy_tickets(new_list)
    if not is_busy_ticket:
        ticket_to_change = start_ticket(ticket_to_change)
    return new_list


def get_ticket_to_change(ticket_name: str, used_tickets: List[Ticket]) -> Ticket:
    ticket_name_small = ticket_name.lower()
    for ticket in used_tickets:
        if ticket.name.lower() == ticket_name_small:
            return ticket
    return Ticket()


def handle_new_ticket(name, used_tickets: List[Ticket]) -> List[str]:
    new_list = used_tickets
    stop_busy_tickets(new_list)
    new_ticket = Ticket(name)
    start_ticket(new_ticket)
    new_list.append(new_ticket)

    return new_list


def rename(original_name: str, new_name: str) -> None:
    used_tickets = get_used_tickets()
    ticket_to_rename = get_ticket_to_change(original_name, used_tickets)
    if ticket_to_rename.name == "":
        error(f"Ticket doesn't seem to exist. ({original_name})")
        return
    log(f"{Fore.GREEN}Found{Style.RESET_ALL} {ticket_to_rename.name}")
    ticket_to_rename.name = new_name
    override_file(used_tickets)
    log(f"Renamed to {Fore.GREEN}{ticket_to_rename.name}{Style.RESET_ALL}")


def update_entry(ticket_name: str) -> None:
    used_tickets = get_used_tickets()
    ticket_to_change = get_ticket_to_change(ticket_name, used_tickets)
    if ticket_to_change.name == "":
        error(f"Ticket doesn't seem to exist. ({ticket_name})")
        return
    update_total_minutes_worked(ticket_to_change)
    override_file(used_tickets)
    return
