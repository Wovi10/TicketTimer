# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import sys
from my_modules import ticket_manager
from my_modules.input_sanitiser import sanitise_script_input
from .my_modules.logger import log


def main(old_name: str, new_name: str):
    log()
    ticket_manager.rename(old_name, new_name)
    log()

if __name__ == "__main__":
    sanitise_script_input(2)
    OLD_NAME = sys.argv[1]
    NEW_NAME = sys.argv[2]
    main(OLD_NAME, NEW_NAME)
