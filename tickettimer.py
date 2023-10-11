import click
from my_modules import ticket_manager, logger

@click.group()
def cli():
    pass

@click.command()
@click.argument('ticket_name')
def entry(ticket_name):
    ticket_manager.add_entry(ticket_name)
    logger.log()

@click.command()
def print_tickets():
    ticket_manager.print_tickets()
    logger.log()

@click.command()
@click.argument('ticket_name')
def delete(ticket_name):
    ticket_manager.delete_entry(ticket_name)

cli.add_command(entry)
cli.add_command(print_tickets)
cli.add_command(delete)

if __name__ == '__main__':
    cli()
