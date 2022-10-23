from settings import *
from support import *
from random import randint

class Enemy:
    def __init__(self, size):
        # board
        self.SIZE = size

        # position
        self.row = 1
        self.col = randint(2, self.SIZE-3)

        # characters for the board
        self.char = colored(ENEMY["color"],ENEMY["char"])