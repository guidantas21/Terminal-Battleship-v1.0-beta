from settings import *
from support import *
from random import randint

class Enemy:
    def __init__(self, size) -> None:
        # board
        self.SIZE = size

        # position
        self.row = 1
        self.col = randint(2, self.SIZE-3)

        # characters for the board
        self.char = colored(ENEMY["color"],ENEMY["char"])
    

    def possible_pos(self) -> list:
        ""

        # 0,1,2
        # 3,E,4
        # 5,6,7
    
        self.all_next_pos = [
            # top
            [self.row-1,self.col-1], # left
            [self.row-1,self.col], # center
            [self.row-1,self.col+1], # right
            # middle 
            [self.row,self.col-1], # left
            [self.row,self.col+1], # right
            # bottom
            [self.row+1,self.col-1], # left
            [self.row+1,self.col], # center
            [self.row+1,self.col+1], # right
        ]

        possible_pos_list = []

        # add only the position that are inside the board
        for pos in self.all_next_pos:
            if self.is_pos_possible(pos):
                possible_pos_list.append(pos)

        return possible_pos_list


    def is_pos_possible(self, p) -> bool:
        "Verify if the position is in the board"

        return p[0] >= 0 and p[0] <= self.SIZE - 1 and p[1] >= 0 and p[1] <= self.SIZE - 1
