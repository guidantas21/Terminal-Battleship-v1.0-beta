from settings import *
from support import *

class Ship:
    def __init__(self, size) -> None:

        # game settings
        self.SIZE = size
        self.coord_letters = ALPHA[0 : self.SIZE]

        # position
        self.row = self.SIZE - 2
        self.col = self.size // 2 

        # characters for the board
        self.char = colored(SHIP["color"], SHIP["char"])
        self.attack_char = colored(ATTACK["color"], ATTACK["char"])

        # variables
        self.shots = SHIP["total shots"]