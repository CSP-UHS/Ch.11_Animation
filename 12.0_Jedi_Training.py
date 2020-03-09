'''

Sign your name: Danny H
All questions are about the final code in Chapter 12:

1.) Where is the ball's original location?
320, 240
2.) What are the variables dx and dy?
the balls x and y movement speed
3.) How many pixels/sec does the ball move in the x-direction?
180 pixels per second
4.) How many pixels/sec does the ball move in the y-direction?
120 pixels per second
5.) Which method is run 60 times/second?
on update
6.) What does this code do?   self.dx *= -1
flips the horizontrol velocity of the ball
7.) What does this code do?  self.pos_y += self.dy
takes the balls old position and adds its momentum to it to make its new up and down position.
8.) What is the width of the window?
640
9.) What is this code checking?  self.pos_y > SH - self.rad:
If the ball is too far down, so it won't go too low and go offscreen
10.) What is this code checking? if self.pos_x < self.rad
if the ball is too far to the left, so it won't go to far and leave the screen


'''