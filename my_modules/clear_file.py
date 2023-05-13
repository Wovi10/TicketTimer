# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
import sys
from .file_adjuster import override_file
from .logger import error

def clear():
    override_file([])
    error("File cleared")
    sys.exit(0)
