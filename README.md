#Capstone Project II

A PyGame (Python) project where the user has to avoid the 3 enemy objects and reach the prize object to win. The user can navigate in any direction using the arrow keys but cannot move beyond the frame. The enemy objects can also not move beyond the frame and bounce off when they reach the frame. As they bounce off their speed increases to make the game challenging and entertaining.

The program makes use of the PyGame and random libraries. The first portion of the code sets the initial variables using functions from the PyGame libary. It also sets the initial positions for all the objecst in the game using the random library. 

The 'game loop' portion of code then runs. This section of code constantly runs while the game is being played. It constantly updates the screen with the correct coordinates of the objects. It also checks whether any input is given by the player. The 'game loop' also monitors whether the enemy objects have collided with the player or whether the player has reached the prize object. If any of those conditions are met then the game would end the 'game loop' resulting in the player either losing or winning.

Robin Titus is the maintainer and contributor of this project.

To run this project, first download it, and then run the following command from your terminal: 'py bounce.py'.
