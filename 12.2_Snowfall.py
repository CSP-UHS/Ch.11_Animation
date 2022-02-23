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
'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''
import arcade
import random
SW = 600
SH = 600

class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx=dx
        self.dy=dy
        self.rad = rad
        self.col = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)
        # arcade.draw_rectangle_filled(self.pos_x,self.pos_y,self.rad,self.rad,self.col,0)
    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        self.col

        #bound ball off wall
        if self.pos_y < 0 - self.rad:
            self.pos_y = SH + self.rad
            self.pos_x = random.randint(0,SW)
        if self.pos_x < 0 - self.rad:
            self.pos_x += self.rad+2+SW
        if self.pos_x > SW + self.rad:
            self.pos_x -= self.rad+2+SW


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)

        self.balls=[]
        for i in range(1000):
            r = random.randint(1,5)
            x = random.randint(r,SW-r)
            y = random.randint(r,SH-r)
            dx = random.random()
            if dx > 0.5:
                dx *= -1
                dx += 0.3
            dy = random.randrange(1,4)
            dy *= -1
            col1 = arcade.color.WHITE
            if i == 0:
                col1 = arcade.color.RED
                r = 5
                dx = 5


            #c=(random.randint(0,225),random.randint(0,255),random.randint(0,225))

            self.ball = Ball(x,y,dx,dy,r,col1)
            self.balls.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        for ball in self.balls:
            ball.draw_ball()
        arcade.draw_rectangle_filled(SW / 2, SH / 2, 5, SW, arcade.color.DARK_BROWN)
        arcade.draw_rectangle_filled(SW / 2, SH / 2, SH, 5, arcade.color.DARK_BROWN)

    def on_update(self,dt):
        for ball in self.balls:
            ball.update_ball()

def myprogram():
    window = MyGame(SW,SH,"Snow fall")
    arcade.run()


if __name__ == "__main__":
    myprogram()
