import sys
from myModules import ticketManager

def main(arg):
    ticketManager.manage(arg)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: A ticketName is required.")
        sys.exit(1)
    param = sys.argv[1]
    main(param)