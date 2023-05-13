# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import sys
from my_modules import ticket_manager
from my_modules.logger import error

def main(arg):
    ticket_manager.add_entry(arg)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        error("Error: A ticketName is required.")
        sys.exit(1)
    PARAM = sys.argv[1]
    main(PARAM)
