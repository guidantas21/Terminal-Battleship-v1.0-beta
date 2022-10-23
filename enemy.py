from settings import *
from support import *
from random import randint, choices

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


    def movement_probability(self, ship_row, ship_col) -> list:
        "Define a the probabilistic weight of each possible position based on the direction tendency"

        direction = self.direction_tendency(ship_row, ship_col)

        debug("Enemy direction tendency", direction)

        # every position starts with the same weight
        prob = [ENEMY["normal weight"] for _ in range(8)]

        # if the position matches with the direction -> higher weight

        # VERTICAL --------------------------------------

        if direction[0] == "down":
            for i in range(5,8):
                prob[i] = ENEMY["high weight"]

        elif direction[0] == "up":
            for i in range(0,3):
                prob[i] = ENEMY["high weight"]

        # HORIZONTAL ------------------------------------

        if direction[1] == "left":
            prob[0] = ENEMY["high weight"]
            prob[3] = ENEMY["high weight"]
            prob[5] = ENEMY["high weight"]

        elif direction[1] == "right":
            prob[2] = ENEMY["high weight"]
            prob[4] = ENEMY["high weight"]
            prob[7] = ENEMY["high weight"]

        return prob
            

    def move(self, ship_row, ship_col) -> None:
        "Move the position of the enemy based on the direction tendency"

        possible_positions = self.possible_pos()

        debug("All possible enemy positions", possible_positions)

        # can move to all position -> diferent probalities of movement based o the direnction tendecy
        if len(possible_positions) == 8:
            prob = self.movement_probability(ship_row, ship_col)

            next_pos_index = choices(range(8), weights=prob)[0]

            debug("Weight of each possible enemy position", prob)
            debug("Enemy next position index", next_pos_index)

        # restrict movement (corner or edge cases) -> same probality of movement
        else:
            next_pos_index = randint(0,len(possible_positions)-1)

        self.row, self.col = possible_positions[next_pos_index]


        
        

        


