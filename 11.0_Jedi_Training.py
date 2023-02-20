'''
Sign your name: Oded Harazi
 
All questions are about the final code in Chapter 12:

1.) Where is the ball's original location?
Anywhere inside the window where the ball(s) can fully be seen.

2.) What are the variables dx and dy?
---The derivatives of x and y. Determine the velocity of the ball and in what direction.

3.) How many pixels/sec does the ball move in the x-direction?
---dx * 60

4.) How many pixels/sec does the ball move in the y-direction?
---dy * 60

5.) Which method is run 60 times/second?
--- "Update" Method (dx and dy)

6.) What does this code do?   self.dx *= -1
---Reverses the direction of the ball.

7.) What does this code do?  self.pos_y += self.dy
---Moves the ball along the y-axis dy pixels, from where it was 60 times per second.

8.) What is the width of the window?
---SW

9.) What is this code checking?  self.pos_y > SH - self.rad:
---Making sure that the ball doesn't float off the top or bottom edge of the window.

10.) What is this code checking? if self.pos_x < self.rad
---Making sure that the ball doesn't float off the right or left edge of the window.




'''
