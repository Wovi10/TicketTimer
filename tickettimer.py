# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import click
from my_modules import clear_file, ticket_manager, logger
from my_modules.input_sanitiser import sanitise_script_input

@click.group()
def cli():
    pass

@click.command()
@click.argument('ticket_name')
def entry(ticket_name):
    """Create/start a ticket

    Args:
        ticket_name (str): The name of the ticket to be created/started
    """
    sanitise_script_input()
    ticket_manager.add_entry(ticket_name)

@click.command()
def print_tickets():
    """Print all tickets of today
    """
    ticket_manager.print_tickets()

@click.command()
@click.argument('ticket_name')
def delete(ticket_name):
    """Delete a specific ticket.

    Args:
        ticket_name (str): The ticket to be deleted (case insensitive)
    """
    sanitise_script_input()
    ticket_manager.delete_entry(ticket_name)

@click.command()
def clear():
    """Clear list file
    """
    clear_file.clear()

@click.command()
def mock_data():
    """Create a list with mock data for testing
    """
    ticket_manager.mock_tickets()

@click.command()
@click.argument('old_name')
@click.argument('new_name')
def rename(old_name, new_name):
    """Rename a ticket

    Args:
        old_name (str): The ticket to be renamed (case insensitive)
        new_name (str): The new name of the ticket
    """
    sanitise_script_input(2)
    ticket_manager.rename(old_name, new_name)

@click.command()
def stop():
    """Stop the currently active ticket
    """
    ticket_manager.stop_entry()

@click.command()
def time_worked():
    """Print the total time worked for today
    """
    ticket_manager.total_time_worked()

@click.command()
def update():
    """Update the currently active ticket and print how long it's been active
    """
    ticket_manager.update_entry()

cli.add_command(entry)
cli.add_command(print_tickets)
cli.add_command(delete)
cli.add_command(clear)
cli.add_command(mock_data)
cli.add_command(rename)
cli.add_command(stop)
cli.add_command(time_worked)
cli.add_command(update)

if __name__ == '__main__':
    cli()
    logger.log()
