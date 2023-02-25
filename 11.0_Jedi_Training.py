"""
Sign your name: Rachel Linthicum

All questions are about the final code in Chapter 11:

1.) Where is the ball's original location?
     - X: between its radius (min) and the screen width minus its radius (max)
     - Y: between its radius (min) and the screen height minus its radius (max)
2.) What are the variables dx and dy?
     - dx = amount of movement side to side for an object
     - dy = amount of movement up and down for an object
3.) How many pixels/sec does the ball move in the x-direction?
     - 60 pixels per second
4.) How many pixels/sec does the ball move in the y-direction?
     - 60 pixels per second
5.) Which method is run 60 times/second?
     - updating the window
6.) What does this code do?   self.dx *= -1
     - multiples -1 to the dx
     - it will turn the ball around instead of continuing the same direction (right will be turned left)
7.) What does this code do?  self.pos_y += self.dy
     - adds the amount of self.dy to the y position
8.) What is the width of the window?
     - 640
9.) What is this code checking?  self.pos_y > SH - self.rad:
     - if the y position of the circle is greater than the screen height - radius
10.) What is this code checking? if self.pos_x < self.rad
     - if the x position is less than the radius (of the circle)
"""
