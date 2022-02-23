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

SW = 600
SH = 600

class Snow():
    def __init__(self, pos_x, pos_y, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_snowflake(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)

    def update_snowflake(self):
        self.pos_y += self.dy

        # respawn snowflake above screen
        if self.pos_y < self.rad:
            self.pos_y = random.randint(600,700)

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowflakes = []
        for i in range(300):
            r = random.randint(1,3)
            x = random.randint(0,600)
            y = random.randint(0,600)
            dy = random.randint(-4,-1)
            if i == 1:
                c = arcade.color.RED
            else:
                c = arcade.color.WHITE
            self.snowflake = Snow(x,y,dy,r,c)
            self.snowflakes.append(self.snowflake)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(SW/2,SH/2,10,SH,arcade.color.RED)
        arcade.draw_rectangle_filled(SW/2,SH/2,SW,10,arcade.color.RED)
        for snowflake in self.snowflakes:
            snowflake.draw_snowflake()
    def on_update(self, dt):
        for snowflake in self.snowflakes:
            snowflake.update_snowflake()

def myprogram():
    window = MyGame(SW,SH,"Snowfall")
    arcade.run()

if __name__ == "__main__":
    myprogram()