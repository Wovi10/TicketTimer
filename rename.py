# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import sys
from my_modules import ticket_manager, logger
from my_modules.input_sanitiser import sanitise_script_input


def main(old_name: str, new_name: str):
    ticket_manager.rename(old_name, new_name)
    logger.log()

if __name__ == "__main__":
    sanitise_script_input(2)
    OLD_NAME = sys.argv[1]
    NEW_NAME = sys.argv[2]
    main(OLD_NAME, NEW_NAME)
