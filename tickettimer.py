import click
from my_modules import clear_file, ticket_manager, logger
from my_modules.input_sanitiser import sanitise_script_input

@click.group()
def cli():
    pass

@click.command()
@click.argument('ticket_name')
def entry(ticket_name):
    sanitise_script_input()
    ticket_manager.add_entry(ticket_name)

@click.command()
def print_tickets():
    ticket_manager.print_tickets()

@click.command()
@click.argument('ticket_name')
def delete(ticket_name):
    sanitise_script_input()
    ticket_manager.delete_entry(ticket_name)

@click.command()
def clear():
    clear_file.clear()

@click.command()
def mock_data():
    ticket_manager.mock_tickets()

@click.command()
@click.argument('old_name')
@click.argument('new_name')
def rename(old_name, new_name):
    sanitise_script_input(2)
    ticket_manager.rename(old_name, new_name)

@click.command()
def stop():
    ticket_manager.stop_entry()

@click.command()
def time_worked():
    ticket_manager.total_time_worked()

@click.command()
def update():
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
