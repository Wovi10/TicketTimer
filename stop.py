# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from my_modules import ticket_manager, logger

def main():
    ticket_manager.stop_entry()
    logger.log()


if __name__ == "__main__":
    main()
