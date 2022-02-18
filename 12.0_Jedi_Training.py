'''
Sign your name:Denis Toric
 
All questions are about the final code in Chapter 12:

1.) Where is the ball's original location?
middle of the screen
2.) What are the variables dx and dy?
Velocity horizontal and vertical
3.) How many pixels/sec does the ball move in the x-direction?
60 pixels per second (180)
4.) How many pixels/sec does the ball move in the y-direction?
60 pixels per second(120)
5.) Which method is run 60 times/second?
 on update/update ball
6.) What does this code do?   self.dx *= -1
dx = opposite/make it go in other direction
7.) What does this code do?  self.pos_y += self.dy
redrawing ball location due to velocity
8.) What is the width of the window?
640 pixels
9.) What is this code checking?  self.pos_y > SH - self.rad:
if ball is off screen on y axis
10.) What is this code checking? if self.pos_x < self.rad
if ball is off screen on x axis left side


'''
class Balls():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.dx=dx
        self.dy=dy
        self.rad=rad
        self.col=col
    def draw_balls(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)
    def update_balls(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        if self.pos_x>SW-self.rad or self.pos_x<self.rad:
            self.dx*=-5
        if self.pos_y > SH - self.rad or self.pos_y < self.rad:
            self.dy *=-5
def on_draw(self):
        arcade.start_render()
        for ball in self.ballslist:
            ball.draw_balls()


def on_update(self, dt):
        for ball in self.ballslist:
            ball.update_balls()
def myprogram():
    window=MyGame(SW,SH,"Window")
    arcade.run()
if __name__=="__main__":
    myprogram()