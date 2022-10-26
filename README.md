# Terminal Battleship v1.0

## Project Overview

1. ### Concept
- This game was inspired by a scene of the movie [Battleship](https://www.imdb.com/title/tt1440129/), in wich the characters have to predict where the enemy will move and attack before he gets there, in order to hit him. So, I thought that maybe it could be fun to program a little game with a similar concept. Basically, you are a ship in a battle with an enemy, but this enemy is not an normal ship, it's way faster and more agile, this way you have to shoot the position that you think the enemy will move to. But, there's a catch: you have limited shots, once run out of shots there's defense against the enemy and you lose, also if it reaches your position, it's gameover. It's important to notice that the enemy always knows where the your ship is, so it's more likely to move in your direction, even if in an unpredictable way. 


2. ### Technology
- [Python](https://www.python.org/) was my language of choice for its conveniece and practicality, given that it is a fairly simple project that runs on terminal, also it doesn't require perfomance at all.
- Another tool that I could exercise a lot was [Git](https://git-scm.com/), one of my requirements for this project was to make use of this version control manager in the proper way (at least in basic things, like committing my changes), and I think I've had a good improvement. 


3. ### Implementation

    1. #### General
    - This project is an exercise of some basics of [Object-Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming), this way, I organized the code in Battleship class (main.py), Ship class (ship.py), Enemy class (enemy.py). Also, I stored the most of the game constants and setting on a seperate file (settings.py), where the user can easily change colors, characters, messages, ASCII arts, total of shots, and even access the debug mode (prints the game information while it's running). To simplify some small details like print colored text, clean the terminal and print debug info, I created functions for all those features that are not directly related to the game in a separate file (support.py)

    2. #### Game
    - The Battlefield class (main.py) is basically resposible to run the game (Battleship().run()), every round it prints the board and status bar, updates the state of the ship and enemy on the board, and check if the enemy got shot (victory) or if the enemy has reached the position of the ship (defeat).

    3. #### Ship
    - The Ship class (ship.py) is really simple, it stores some ship attributes like: character, attack character, position and the number of shots you have. The only action the ship does is attack, so we have a method to get a valid coordenate input (Ship()input_attack()) and a method to translate those board coordenates into 2 dimensional array coordenates and return it (Ship().attack()), those coordenates will be used by the Battleship class update the attack on the board.

    4. #### Enemy
    - The Enemy class (enemy.py) is the most fun, also the most complex (is not complex, but I spent more time figuring out this one), it stores the enemy character and position. So, for the implemantation of the algorithm of movement I wanted something the was not completely random, but also not completely predictable, this way a came up with a logic different of probabilites of movement based on the position of the the ship. The algorithm explanation:

        1. Get all possible positions:
            - As the enemy can move 1 node per round, it can go up (row-1,col), down (row+1,col), left (row,col-1), right (row,col+1), up left (row-1,col-1), down left (row+1,col-1), up right (row-1,col+1), down right (row+1,col+1)

        2. Get only the valid positions:
            - For example, If the enemy reached the to of the board, it cannot move up, up right or up left, those are invalid moves. We want only the positions that the enemy is allowed to move to.

        3. Get the direction tendency:
            - For this step, we need to know the position of the ship, once we want to define the direction of the in relation to the enemy. To do that, we compare the the rows and columns, for example: if the enemy row is greater than the ship row, the enemy needs to move down, and if enemy col is less than ship col, the enemy needs to move right. The result is an array with the row direction and the column direction [down, right]. 
        
        4. Define the probability (weight) of each position:
            - Based on the direction tendecy, we are going to define the which positions the enemy is more likely to move. Basically, we are going to create an array with the weight of each position, there are 2 types of weight (defined on setting.py): normal weight (1 by default) and high weight (2 by default). NOT FINISHED

    5. #### ASCII art


4. ### Ideas for the next version

    1. #### Different enemy behaviors
    - For this version the enemy only has one behavior, which is to have higher chance to go indirection to the ship, that's okay, but still feels kinda random and artificial. 
    - So, imagine if the enemy could have different the possibility to be more agressive (more dangerous to the player, but more predictable) or defensive (movements hard to predict, but rarely gets close to the ship).

    2. #### Multiple ship actions
    - Currently, our only possible action is to shoot the enemy, but now the behavior of the enemy is not always the same, this way would be interesting to have the option of not attacking, so we save shot and can understand the tendency of the enemy. Also, as the enemy can get very agressive the ship should be able to choose to move, so can scape from the range of movement of the enemy.

    4. #### More ASCII art
    - Don't get me wrong, the art that I got from the internet is very cool, but I like to combine things and make a more specific thing for the game and what I did was kinda improvised... so for the next version it would be nice to have more detailed ASCII art and texts. 

## How to run
- TODO (Necessary push the project to GitHub)


## How to play

1. ### Objective
- The gameplay is very simple, you have a cartesian plane (board) in which you can see your ship (represented by "S") and an enemy(represented by "E"). Your objective is to shot the position the enemy is going to move to, basically predict his movement, to do so you have to input the coordenates of your shot. If you run out of bullets or if the enemy reaches your position it's gameover.

2. ### Input coordenates
- The x axis is represented by letters (top of the board) and the y axis is represented by numbers (left side of the board). To input the coordenates you only need write an letter and the number, for example: A2, 2a, 3d, C4.

3. ### Gameplay tip
- To help you, I'm going to give you a little tip: the enemy movement is not completely random and it always knows position of your ship (algorithm explained on the Implementation section).
- The enemy can only move 1 node per turn.  


## References
- [SHIP ASCII ART](https://www.asciiart.eu/vehicles/navy)
- [EXPLOSION ASCII ART](https://www.asciiart.eu/weapons/explosives)
- [ASCII TEXT](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)