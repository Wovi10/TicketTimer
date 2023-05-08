# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
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
