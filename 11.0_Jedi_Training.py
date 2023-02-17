'''
Sign your name:Aidan Zimmerman
 
All questions are about the final code in Chapter 12:

1.) Where is the ball's original location?
We randomized everything, so I forgot what the original position was

2.) What are the variables dx and dy?
The change in x or y every 1/60th of a second

3.) How many pixels/sec does the ball move in the x-direction?
120 - I think this was the original pixels/sec because I think dx was equal to 2

4.) How many pixels/sec does the ball move in the y-direction?
180 - I think dy was equal to 3

5.) Which method is run 60 times/second?
    def on_update(self, dt):
        for item in (self.ball_list):
            item.update_ball()

6.) What does this code do?   self.dx *= -1
It reverses the rate so the object will go the other way/bounce off the wall

7.) What does this code do?  self.pos_y += self.dy
That adds the rate of change to the position making the object move forward

8.) What is the width of the window?
640,480

9.) What is this code checking?  self.pos_y > SH - self.rad:
It is checking if the object is outside of the top of the screen

10.) What is this code checking? if self.pos_x < self.rad
It is checking if the object is outside the left side of the screen



'''
