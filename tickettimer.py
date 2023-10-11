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



cli.add_command(entry)

if __name__ == '__main__':
    cli()
