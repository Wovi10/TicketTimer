import sys
from my_modules import ticket_manager

def main(arg):
    ticket_manager.manage(arg)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: A ticketName is required.")
        sys.exit(1)
    PARAM = sys.argv[1]
    main(PARAM)
