from settings import *
from support import *
from ship import Ship
from enemy import Enemy


class Battleship:
    def __init__(self, size=SIZE["default"]) -> None:
        
        # BOARD --------------------

        # size 
        if self.is_size_valid(size):
            self.SIZE = size
        else:
            self.SIZE = SIZE["default"]

        # coord letters -> cols: letters (A,B,C,...) rows: numers (1,2,3..) 
        self.coord_letters = ALPHA[0 : self.SIZE]

        # grid character -> each node of the grid is represented by a character
        self.grid_char = colored(GRID["color"], GRID["char"])


        # OBJECTS -------------------

        self.ship = Ship(self.SIZE)
        self.enemy = Enemy(self.SIZE)


    def is_size_valid(self, size) -> bool:
        "Check if the passed size is valid"

        return SIZE["min"] <= size <= SIZE["max"]

    
    def empty_board(self) -> list:
        "Create a 2d list that represents the game board empty"

        return [[self.grid_char for j in range(self.SIZE)] for i in range(self.SIZE)]

    
    def print_board(self) -> None:
        "Print the game board on the terminal"

        # colored row coord indicators -> A, B, C, D ...
        print(' ', end="    ")
        for l in self.coord_letters:
            print(colored(GRID["coord color"], l), end="    ")
        
        print("\n")

        # colored row coord inidcators -> 1, 2, 3, 4 ...
        for n,i in enumerate(range(self.SIZE)):
            print(colored(GRID["coord color"], n+1), end="    ")

            # each element of the board
            for j in range(self.SIZE):
                print(self.board[i][j], end="    ")

            print("\n")


    def update_board(self) -> None:
        "Update the state of the board and of the elements on it"

        # empty board
        self.board = self.empty_board()

        # add ship to the board
        self.board[self.ship.row][self.ship.col] = self.ship.char

        # add enemy to the board
        self.board[self.enemy.row][self.enemy.col] = self.enemy.char


    def run(self) -> None:
        "Execute the game"

        while True:
            clean_terminal()

            debug("Board size", self.SIZE)
            debug("Grid character", self.grid_char)
            debug("Enemy char", self.enemy.char)
            debug("Ship char", self.ship.char)
            
            self.update_board()
            self.print_board()

            debug("Enemy position", (self.enemy.row, self.enemy.col))
            debug("Ship position", (self.ship.row, self.ship.col))
            debug("Ship shots", self.ship.shots)
            
            # move enemy

            attack_input = self.ship.input_attack_coord()

            debug("Attack input", attack_input)









if __name__ == "__main__":
    Battleship().run()