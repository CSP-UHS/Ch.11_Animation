'''
Sign your name:________________
 
All questions are about the final code in Chapter 12:

1.) Where is the ball's original location?
320,240

2.) What are the variables dx and dy?
dx is the velocity of the ball in the direction of the x-axis
dy is the velocity of the ball in the direction of the y-axis

3.) How many pixels/sec does the ball move in the x-direction?
180 pixels per second

4.) How many pixels/sec does the ball move in the y-direction?
120 pixels per second

5.) Which method is run 60 times/second?
The on_update method

6.) What does this code do?   self.dx *= -1
It will change the direction of the velocity of the ball according to the x-axis.

7.) What does this code do?  self.pos_y += self.dy
It's changing the the ball's direction every time (up and down)

8.) What is the width of the window?
640

9.) What is this code checking?  self.pos_y > SH - self.rad:
If the y position is greater than the screen's height minus the ball's radius. If it's going off the top of the screen

10.) What is this code checking? if self.pos_x < self.rad
If the x position is greater than the ball's radius. If the ball is going off the left side of the screen.


'''
