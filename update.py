# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from my_modules import ticket_manager
from .my_modules.logger import log

def main():
    log()
    ticket_manager.update_entry()
    log()


if __name__ == "__main__":
    main()
