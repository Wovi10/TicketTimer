# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring
from colorama import Fore, Back, Style

def log(text = ""):
    print(text + Style.RESET_ALL)


def error(text = "", back_colour = Back.BLACK):
    print(Fore.RED + back_colour + text + Style.RESET_ALL)
