import sys
from my_modules import ticket_manager
from my_modules.logger import error


def main(old_name: str, new_name: str):
    ticket_manager.rename(old_name, new_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        error("Error: Both an old and new name are required.")
        sys.exit(1)
    if len(sys.argv) < 3:
        error("Error: A new name is required.")
        sys.exit(1)
    OLD_NAME = sys.argv[1]
    NEW_NAME = sys.argv[2]
    main(OLD_NAME, NEW_NAME)
