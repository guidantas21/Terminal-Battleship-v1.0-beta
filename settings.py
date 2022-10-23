DEBUG = True

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

COLORS = {
    "red": (255,0,0),
    "green": (0,255,0),
    "blue": (0,0,255),
    "light blue": (0,128,128),
    "white": (255,255,255)
}

SHIP = {
    "color": COLORS["blue"],
    "char": "S",
    "total shots": 10,
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