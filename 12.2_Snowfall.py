'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

    # 1.) Create a 600 x 600 window with black background
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

class snow_ball:
    def __init__(self, pos_x, pos_y, dy, col):
        self.radius = random.randint(1, 3)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.col = col
    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.col)
    def update_ball(self):
        self.pos_y += self.dy

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.snowlist = []
        for i in range(300):
            self.snow_ball = snow_ball(random.randint(0, 600),random.randint(0,600),random.randint(-4,1), arcade.color.WHITE)
            self.snowlist.append(self.snow_ball)

    def on_draw(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.draw_rectangle_filled(300,300,10,600,arcade.color.RED_BROWN) # Y
        arcade.draw_rectangle_filled(300,300,600,10, arcade.color.RED_BROWN)

def main():
    SH = 600
    SW = 600
    window = MyGame(SH,SW, "SnowFall")
    arcade.run()

main()
