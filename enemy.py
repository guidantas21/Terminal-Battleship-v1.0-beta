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
        "Get all possitions that the Enemy can move to"

        #  ___________________________________
        # |E,0    0,1,2      0,E,1        0,E|
        # |1,2    3,E,4      3,4,5        1,2|
        # |       5,6,7                      |
        # |0,1                            0,1|
        # |E,2                            2,E|
        # |3,4                            3,4|
        # |                                  |
        # |0,1        0,1,2               0,1|
        # |E,2        3,E,4               2,E|
        # ------------------------------------

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

    
    def direction_tendency(self, ship_row, ship_col) -> list:
        "Define the direction the enemy is more likely to move based on the ship position"

        direction = [None, None]

        # VERTICAL ------------------------------------------ 

        # if ship is belllow the enemy -> tendency to move down
        if self.row < ship_row:
            direction[0] = "down"
        # if enemy is bellow the ship -> tendency to move up
        elif self.row > ship_row:
            direction[0] = "up"
        # if in the same row -> tendency to stay there
        else:
            direction[0] = None

        # HORIZONTAL ----------------------------------------

        # if ship is on the right -> tendency to move right
        if self.col < ship_col:
            direction[1] = "right"
        # if ship is on the left -> tendency to move left
        elif self.col > ship_col:
            direction[1] = "left"
        # if in the same col -> tendency to stay there
        else:
            direction[1] = None
        
        return direction
