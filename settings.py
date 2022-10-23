from ascii_text import *

COLORS = {
    "white": (255,255,255),
    "red": (255,0,0),
    "yellow": (255,255,0),
    "green": (0,255,0),
    "blue": (0,0,255),
    "light blue": (0,128,128),
}

ASCII_ART = {
    "logo": LOGO_ASCII,
    "title": TITLE_SLANT_ASCII,
    "victory": VICTORY_ASCII,
    "defeat": DEFEAT_ASCII
}

DEBUG = {
    "active": False,
    "color": COLORS["light blue"]
}

CLEAN_TERMINAL = True

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

SIZE = {
    "default": 9,
    "max": 26,
    "min": 6
}


ENEMY = {
    "color": COLORS["red"],
    "char": "E",
    "high weight": 5,
    "normal weight": 1
}

SHIP = {
    "color": COLORS["blue"],
    "char": "S",
    "total shots": 10,
    "messages": {
        "input attack coord": "(input) Input attack coordenates: ",
        "invalid input": "(error) Invalid input, try again! (ex: a2 or d3)",
        "ship fire": f"(invalid) You inputed the coordenate of the ship! Shoot the enemy ({ENEMY['char']}) position."
    }
}

GRID = {
    "color": COLORS["white"],
    "coord color": COLORS["green"],
    "char": "+"
}

ATTACK = {
    "color": COLORS["light blue"],
    "char": "X"
}
