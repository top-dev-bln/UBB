import os
import platform


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def print_green(text):
    print(f"\033[32m{text}\033[0m")


def print_red(text):
    print(f"\033[31m{text}\033[0m")


def press_any_key_to_continue():
    input("Press any key to continue: ")
