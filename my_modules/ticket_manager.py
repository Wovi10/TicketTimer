# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import json
from datetime import datetime
from typing import List
from . import TIME_FORMAT, DATE_FORMAT, FILENAME, READ_MODE, DEFAULT_ENCODING
from .ticket import Ticket
from .shared_code import override_file


def manage(ticket_name: str):
    used_tickets: List[Ticket] = get_used_tickets()
    used_ticket_names: List[str] = [ticket.name for ticket in used_tickets] or []

    new_list = used_tickets

    if is_used_ticket(ticket_name, used_ticket_names):
        new_list = handle_used_ticket(ticket_name, new_list)
    else:
        new_list = handle_new_ticket(ticket_name, new_list)
    override_file(new_list)


def get_used_tickets() -> List[Ticket]:
    try:
        with open(FILENAME, READ_MODE, encoding=DEFAULT_ENCODING) as f:
            data = json.load(f)
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


def is_used_ticket(ticket_name: str, used_ticket_names: List[str]) -> bool:
    return ticket_name in used_ticket_names


def handle_used_ticket(ticket_name: str, used_tickets: List[Ticket]) -> List[str]:
    new_list = used_tickets
    ticket_to_change = get_ticket_to_change(ticket_name, new_list)
    is_busy_ticket = ticket_to_change.busy
    new_list = stop_busy_tickets(new_list)
    if not is_busy_ticket:
        ticket_to_change = start_ticket(ticket_to_change)
    return new_list


def get_ticket_to_change(ticket_name: str, used_tickets: List[Ticket]) -> Ticket:
    for ticket in used_tickets:
        if ticket.name == ticket_name:
            return ticket
    return Ticket()


def stop_busy_tickets(used_tickets: List[Ticket]) -> List[Ticket]:
    new_list = used_tickets
    print("Going over tickets")
    for ticket in new_list:
        print(f"\t- {ticket.name}")
        if not ticket.busy:
            print("\t\tSkipped")
            continue

        total_minutes = calculate_total_minutes(ticket)
        ticket.timeWorkedInMinutes += total_minutes
        print(f"\t\tWorked {ticket.timeWorkedInMinutes} minutes")
        ticket.busy = False
        print("\t\tStopped")
    print()
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
    print(f"Started {ticket.name}")
    return ticket


def handle_new_ticket(name, used_tickets: List[Ticket]) -> List[str]:
    new_list = used_tickets
    stop_busy_tickets(new_list)
    new_ticket = Ticket(name)
    start_ticket(new_ticket)
    new_list.append(new_ticket)

    return new_list
