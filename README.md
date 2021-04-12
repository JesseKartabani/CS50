# Snake
#### Video Demo: https://youtu.be/9jpWAdqM3q4
#### Description: 
This is a remake of the classic snake game, made with the pygame module and Python3.
main.py is responsible for running the enitre game.

Design: There are many ways to go about designing snake. So how are we going to do this?
By using the redrawWindow function I fist filled the screen with black and drew out a grid. 
Then for making the snake, our snake object is going to contain a list of cubes which will 
represent the snakes body, we also want to draw eyes on the first cube.
Lastly i needed to add random cubes to the grid for the snake to eat or collect.

Snake movement: The snake is controlled using the up, down, left and right arrow keys.
To allow the snake to move I made the move() function. the most complicated part of making
the game was turning the snake. I needed to remember where the snake was turned and which
direction so that when the cubes before the head reached that spot i could turn them as well.
This is why whenever we turn we add the position of our head to a turn dictionary where the
value is the direction we turned. This way when the other cubes reach this position we know
which way to turn them.

Running the game: I didnt want the game to be run through the command line so i created a batch
file so i could run it using a desktop icon instead and also give it a unique picture.

