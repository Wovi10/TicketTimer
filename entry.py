# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import sys
from .my_modules import ticket_manager
from .my_modules.logger import log
from .my_modules.input_sanitiser import sanitise_script_input

def main(arg):
    log()
    ticket_manager.add_entry(arg)
    log()

if __name__ == "__main__":
    sanitise_script_input()
    PARAM = sys.argv[1]
    main(PARAM)
