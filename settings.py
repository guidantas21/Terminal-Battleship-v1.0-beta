COLORS = {
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255),
    "light blue": (0,128,128),
    "white": (255,255,255)
}

DEBUG = {
    "active": True,
    "color": COLORS["light blue"]
}


CLEAN_TERMINAL = False

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

SIZE = {
    "default": 9,
    "max": 26,
    "min": 6
}

MESSAGES = {
    "victory": "VICTORY!",
    "defeat": "DEFEAT!"
}

SHIP = {
    "color": COLORS["blue"],
    "char": "S",
    "total shots": 10,
    "messages": {
        "input attack coord": "(input) Input attack coordenates: ",
        "invalid input": "(error) Invalid input, try again! (ex: a2 or d3)"
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

ENEMY = {
    "color": COLORS["red"],
    "char": "E",
    "high weight": 5,
    "normal weight": 1
}