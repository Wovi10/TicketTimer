# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import json
from datetime import datetime
from pathlib import Path
from typing import List
from colorama import Fore, Style

from . import DATE_FORMAT, FILENAME, READ_MODE, DEFAULT_ENCODING
from .logger import log, error
from .ticket import Ticket
from .file_adjuster import (override_file, stop_busy_tickets,
                            start_ticket, stop_ticket, update_total_minutes_worked)


def add_entry(ticket_name: str) -> None:
    used_tickets: List[Ticket] = get_used_tickets()
    used_ticket_names: List[str] = [ticket.name for ticket in used_tickets] or []

    new_list = used_tickets

    if ticket_name in used_ticket_names:
        new_list = handle_used_ticket(ticket_name, new_list)
    else:
        new_list = handle_new_ticket(ticket_name, new_list)
    override_file(new_list)


def get_used_tickets() -> List[Ticket]:
    try:
        if not Path(FILENAME).is_file():
            return []
        with open(FILENAME, READ_MODE, encoding=DEFAULT_ENCODING) as file:
            data = json.load(file)
        used_tickets = [Ticket(**ticket) for ticket in data[0]]

        date: str = used_tickets[0].date or datetime.now().strftime(DATE_FORMAT)
        if date != datetime.now().strftime(DATE_FORMAT):
            return []
        return used_tickets
    except json.JSONDecodeError:
        return []


def clean_file(used_tickets: List[Ticket]) -> List[Ticket]:
    new_list = []
    for ticket in used_tickets:
        date: str = ticket.date or datetime.now().strftime(DATE_FORMAT)
        if date == datetime.now().strftime(DATE_FORMAT):
            new_list.append(ticket)
    override_file(new_list)
    return new_list


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


def get_active_ticket(used_tickets: List[Ticket]) -> Ticket:
    for ticket in used_tickets:
        if ticket.busy is True:
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
    existing_ticket = get_ticket_to_change(new_name, used_tickets)
    if existing_ticket.name != "":
        existing_ticket.timeWorkedInMinutes += ticket_to_rename.timeWorkedInMinutes
        stop_ticket(ticket_to_rename)
        start_ticket(existing_ticket)
        used_tickets = handle_delete_ticket(ticket_to_rename.name, used_tickets)
    else:
        ticket_to_rename.name = new_name

    override_file(used_tickets)
    log(f"Renamed to {Fore.GREEN}{new_name}{Style.RESET_ALL}")


def update_entry() -> None:
    used_tickets = get_used_tickets()
    ticket_to_change = get_active_ticket(used_tickets)
    if ticket_to_change.name == "":
        error("No active ticket was found.")
        return
    log(f"{Fore.GREEN}Found{Style.RESET_ALL} {ticket_to_change.name}")
    update_total_minutes_worked(ticket_to_change)
    override_file(used_tickets)
    return


def print_tickets() -> None:
    used_tickets = get_used_tickets()
    if len(used_tickets) <= 0:
        error("No tickets were logged just yet.")
        log()
        return
    log("Printing all tickets of today:")
    for ticket in used_tickets:
        ticket.to_string()
    log()
    return


def delete_entry(ticket_name: str):
    used_tickets: List[Ticket] = get_used_tickets()
    used_ticket_names: List[str] = [ticket.name for ticket in used_tickets] or []

    new_list = used_tickets

    if ticket_name in used_ticket_names:
        new_list = handle_delete_ticket(ticket_name, new_list)
    else:
        error("Didn't find ticket.")
    override_file(new_list)


def handle_delete_ticket(ticket_name: str, used_tickets: List[Ticket]) -> List[Ticket]:
    new_list = used_tickets
    ticket_to_delete = None
    for ticket in new_list:
        if ticket.name.lower() == ticket_name.lower():
            ticket_to_delete = ticket
            continue
    if ticket_to_delete is not None:
        new_list.remove(ticket_to_delete)
        log("Ticket deleted")

    return new_list


def stop_entry():
    used_tickets = get_used_tickets()
    ticket_to_change = get_active_ticket(used_tickets)
    if ticket_to_change.name == "":
        error("No active ticket was found.")
        return
    stop_ticket(ticket_to_change)
    override_file(used_tickets)
    return


def total_time_worked():
    used_tickets = get_used_tickets()
    total_minutes = 0
    for ticket in used_tickets:
        if ticket.timeWorkedInMinutes >= 0:
            total_minutes += ticket.timeWorkedInMinutes
    log(f"Worked {Fore.GREEN}{total_minutes}{Fore.RESET} minutes today")


def mock_tickets():
    tickets: List[Ticket] = []
    for _ in range(0,5):
        ticket = Ticket("Mock")
        ticket.set_defaults()
        tickets.append(ticket)
    override_file(tickets)
