# Snake
#### Video Demo: https://youtu.be/9jpWAdqM3q4
#### Description: 

A snake game is an arcade maze game which has been developed by Gremlin Industries and 
published by Sega in October 1976. It is considered to be a skillful game and has 
popularized among people for generations. The snake in the Snake game is controlled using
the four directon buttons relative to the direction its headed in. The player's objective
in the game is to achieve maxium points as possible by collecting food or fruits. The
player loses once the snake hits the wall or hits itself.

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

Adding food: Now that my snake can move around the screen i need something for it to eat or collect.
Every time we colide with one of these objects we will add a new cibe to the end of our snake.
We are going to call this item a snack.

The first step to generate a posititon for our "snack". I did this inside the randomSnack()
function.

Running the game: I didnt want the game to be run through the command line so i created a batch
file using this syntax 
"C:\Users\Jesse\Desktop\Code\python.exe" 
"C:\Users\Jesse\Desktop\CS50\FinalProject\Snake\main.py"
pause
so i could run it using a desktop icon instead and also give it a unique picture.

More info on pygame:
https://www.javatpoint.com/pygame




