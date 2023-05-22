# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from my_modules import clear_file
from .my_modules.logger import log

def main():
    log()
    clear_file.clear()
    log()

if __name__ == "__main__":
    main()
