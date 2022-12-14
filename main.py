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

        # FUNCTIONS -----------------

        self.place_elements()

        # VARIABLES -----------------
        self.round = 0
        self.active = True


    def is_size_valid(self, size) -> bool:
        "Check if the passed size is valid"

        return SIZE["min"] <= size <= SIZE["max"]

    
    def empty_board(self) -> list:
        "Create a 2d list that represents the game board empty"

        return [[self.grid_char for j in range(self.SIZE)] for i in range(self.SIZE)]


    def place_elements(self) -> None:
        "Place the basic elements on the board"

        # empty board
        self.board = self.empty_board()

        # add ship to the board
        self.board[self.ship.row][self.ship.col] = self.ship.char

        # add enemy to the board
        self.board[self.enemy.row][self.enemy.col] = self.enemy.char

    
    def print_board(self) -> None:
        "Print the game board on the terminal"

        # colored row coord indicators -> A, B, C, D ...
        print("\t\t\t\t ", end="")
        for l in self.coord_letters:
            print("\t",colored(GRID["coord color"], l), end="")
        
        print("\n")

        # colored row coord inidcators -> 1, 2, 3, 4 ...
        for n,i in enumerate(range(self.SIZE)):
            print("\t\t\t\t",colored(GRID["coord color"], n+1), end="")

            # each element of the board
            for j in range(self.SIZE):
                print("\t",self.board[i][j], end="")

            print("\n")

        print("\n")

    
    def print_status(self) -> None:
        "Print game status"

        print(f"Round: {self.round}  Shots: {self.ship.shots}  Ship: {self.ship.char}  Enemy: {self.enemy.char}  Attack: {self.ship.attack_char}")


    def update_board(self) -> None:
        "Update the state of the board and of the elements on it"

        # change enemy position
        self.enemy.move(self.ship.row, self.ship.col)

        # add elements to the board
        self.place_elements()

        # get attack coordenates
        self.attack_row, self.attack_col = self.ship.attack()

        # add attack inidicator to the board
        self.board[self.attack_row][self.attack_col] = self.ship.attack_char


    def defeat(self) -> None:
        "Lose the game"

        clean_terminal()
        print(colored(COLORS["red"],ASCII_ART["defeat"]))

        self.active = False


    def victory(self) -> None:
        "Win the game"

        clean_terminal()
        print(colored(COLORS["blue"],ASCII_ART["victory"]))

        self.active = False


    def check_gameover(self) -> None:
        "Verify if there's victory ou defeat"

        if self.ship.shots <= 0:
            self.defeat()
        
        elif self.attack_row == self.enemy.row and self.attack_col == self.enemy.col:
            self.victory()


    def run(self) -> None:
        "Execute the game"

        while self.active:
            clean_terminal()

            self.round += 1
            print(colored(COLORS["white"],LOGO_ASCII))
            self.print_board()
            self.print_status()
            self.update_board()
            self.check_gameover()
            


if __name__ == "__main__":
    Battleship().run()