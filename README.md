# Terminal Battleship v1.0

## Project Overview

1. ### Concept
- This game was inspired by a scene of the movie [Battleship](https://www.imdb.com/title/tt1440129/), in wich the characters have to predict where the enemy will move and attack before he gets there, in order to hit him. So, I thought that maybe it could be fun to program a little game with a similar concept. Basically, you are a ship in a battle with an enemy, but this enemy is not an normal ship, it's way faster and more agile, this way you have to shoot the position that you think the enemy will move to. But, there's a catch: you have limited shots, once run out of shots there's defense against the enemy and you lose, also if it reaches your position, it's gameover. It's important to notice that the enemy always knows where the your ship is, so it's more likely to move in your direction, even if in an unpredictable way. 


2. ### Technology
- [Python](https://www.python.org/) was my language of choice for its conveniece and practicality, given that it is a fairly simple project that runs on terminal, also it doesn't require perfomance at all.
- Another tool that I could exercise a lot was [Git](https://git-scm.com/), one of my requirements for this project was to make use of this version control manager in the proper way (at least in basic things, like committing my changes), and I think I've had a good improvement. 


3. ### Implementation

    1. #### General

    2. #### Game

    3. #### Ship

    4. #### Enemy

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