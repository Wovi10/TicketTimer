import sys
from .logger import error

def sanitise_script_input(num_args = 1) -> None:
    if num_args == 2:
        sanitise_double_input()

    if len(sys.argv) < 2:
        error("Error: A ticketName is required.")
        sys.exit(1)


def sanitise_double_input() -> None:
    if len(sys.argv) < 2:
        error("Error: Both an old and new name are required.")
        sys.exit(1)
    if len(sys.argv) < 3:
        error("Error: A new name is required.")
        sys.exit(1)
