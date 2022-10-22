from settings import *
from support import *

class Battleship:
    def __init__(self, size=SIZE["default"]) -> None:
        
        # board size 
        if self.is_size_valid(size):
            self.SIZE = size
        else:
            self.SIZE = SIZE["default"]

    def is_size_valid(self, size):
        "Check if the passed size is valid"

        return SIZE["min"] <= size <= SIZE["max"]

    def run(self):
        "Execute the game"

        print(self.SIZE)



if __name__ == "__main__":
    Battleship().run()