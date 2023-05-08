import sys
from . import override_file

def clear():
    override_file([])
    print("File cleared")
    print()
    print()
    print()
    print()
    sys.exit(0)
