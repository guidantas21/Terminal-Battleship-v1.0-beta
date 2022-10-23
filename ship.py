from settings import *
from support import *

class Ship:
    def __init__(self, size) -> None:

        # game settings
        self.SIZE = size
        self.coord_letters = ALPHA[0 : self.SIZE]

        # position
        self.row = self.SIZE - 2
        self.col = self.SIZE // 2 

        # characters for the board
        self.char = colored(SHIP["color"], SHIP["char"])
        self.attack_char = colored(ATTACK["color"], ATTACK["char"])

        # variables
        self.shots = SHIP["total shots"]

    
    def input_attack_coord(self) -> list:
        "Input the coordenate os the attack, ex: A2 or 3D"

        while True:
            # get user first two char of uppercase user input
            coord = str(input(SHIP["messages"]["input attack coord"])).upper()[0:2].strip()

            # check format "2A" (letter before number) and if it is on the board
            if coord[0].isdigit() and not coord[1].isdigit():
                if 0 < int(coord[0]) < self.SIZE and coord[1] in self.coord_letters:
                    return coord[::-1]

             # check format "A2" (number before letter) and if it is on the board
            elif not coord[0].isdigit() and coord[1].isdigit():
                if 0 < int(coord[1]) < self.SIZE and coord[0] in self.coord_letters:
                    return coord

            print(colored(COLORS["red"],SHIP["messages"]["invalid input"]))
