# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import sys
from my_modules import ticket_manager
from my_modules.input_sanitiser import sanitise_script_input

def main(arg):
    ticket_manager.delete_entry(arg)

if __name__ == "__main__":
    sanitise_script_input()
    PARAM = sys.argv[1]
    main(PARAM)
