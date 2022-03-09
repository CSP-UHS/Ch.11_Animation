'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''
import arcade
import random
SW=600
SH=600
class Ball():
    def __init__(self,pos_x,pos_y,dy,rad,col):
        self.pos_x=pos_x
        self.pos_y=pos_y

        self.dy=dy
        self.rad=rad
        self.col=col
    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)
    def update_ball(self):

        self.pos_y+=self.dy

        if self.pos_x>SW-self.rad or self.pos_x<self.rad:
            self.pos_y=600+random.randint(1,100)

        if self.pos_y<self.rad:
            self.pos_y=SH+random.randint(1,100)

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)
        self.balls=[]
        for i in range(1):
            r=random.randint(1,4)
            x=random.randint(r,SW-r)
            y=random.randint(r,SH-r)
            dy=random.randint(-3,-1)
            c=arcade.color.RED_DEVIL
            ball=Ball(x,y,dy,r,c)
            self.balls.append(ball)
        for i in range(299):
            r = random.randint(1, 4)
            x = random.randint(r, SW - r)
            y = random.randint(r, SH - r)
            dy = random.randint(-1, -1)
            c = arcade.color.WHITE
            ball = Ball(x, y, dy, r, c)
            self.balls.append(ball)
    def on_draw(self):
        arcade.start_render()
        for ball in self.balls:
            ball.draw_ball()
        arcade.draw_rectangle_filled(SW/2,SH/2,SW,10,arcade.color.RED_BROWN)
        arcade.draw_rectangle_filled(SW/2,SH/2,10,SH,arcade.color.RED_BROWN)
    def on_update(self, dt):
        for ball in self.balls:
            ball.update_ball()
def myprogram():
   window=MyGame(SW,SH,"Drawing Example")
   arcade.run()

if __name__=="__main__":
    myprogram()






