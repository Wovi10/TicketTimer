# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from my_modules import clear_file, logger

def main():
    clear_file.clear()
    logger.log()

if __name__ == "__main__":
    main()
