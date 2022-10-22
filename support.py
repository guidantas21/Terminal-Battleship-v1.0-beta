from settings import *
from os import system

def colored(rgb, text):
    "Return colored (r,g,b) text"

    return f"\033[38;2;{rgb[0]};{rgb[1]};{rgb[2]}m{text}\033[38;2;255;255;255m"

def debug(text, info):
    "Log info for debug some info while the game is running"

    if DEBUG:
        print(f"(debug) {text}: {info}")

def clean_terminal():
    "Clean terminal"

    if CLEAN_TERMINAL:
        system("cls")