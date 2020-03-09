'''
Sign your name:Malsawmthara Hmar
 
All questions are about the final code in Chapter 12:

1.) Where is the ball's original location?
It is at x 320, and y 240
2.) What are the variables dx and dy?
Dx is how many pixel an object is moved in one 60th of a second following the x coordinate.Dy is how many pixel an object is moved in one 60th of a second following y coodinate.
dx=3, dy=2
3.) How many pixels/sec does the ball move in the x-direction?
The ball moves 180 pixels/sec in x-direction.
4.) How many pixels/sec does the ball move in the y-direction?
The ball moves 120 pixels/sec in y-direction.
5.) Which method is run 60 times/second?
On_update method is run 60 times/second.
6.) What does this code do?   self.dx *= -1
The Object will go opposite direction of the dx it is going.
7.) What does this code do?  self.pos_y += self.dy
It adds the value of dy into pos_y, it makes the ball goes up or down.
8.) What is the width of the window?
It is 640 pixels.
9.) What is this code checking?  self.pos_y > SH - self.rad:
It checks the y position of the object if it is more than the value of screen height minus the object's radius.
It is checking if the top of the screen is being hit by the ball.
10.) What is this code checking? if self.pos_x < self.rad
I checks the x position of the object if it is less than the radius of the object.
It is checking if the bottom of the screen is hit by the bottom of the ball.

'''
