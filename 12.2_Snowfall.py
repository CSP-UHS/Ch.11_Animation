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
class Snowflakes():
    def __init__(self, x, y, rad, dy, col):
        self.x = x
        self.y = y
        self.rad = rad
        self.dy = dy
        self.col = col
    def draw_snowflake(self):
        arcade.draw_circle_filled(self.x, self.y, self.rad, self.col)
    def update_snowflake(self):
        self.y += self.dy
        if self.y <= 1:
            self.y = 600
            if self.x >= 295 and self.x <= 305:
                self.x += 20
class Snowfall(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.list = []
        for i in range(300):
            if i != 299:
                self.snowflake = Snowflakes(random.randrange(0,601),random.randrange(0,601), random.randrange(1,4),random.randrange(-4,0),arcade.color.WHITE)
            else:
                self.snowflake = Snowflakes(random.randrange(0, 601), random.randrange(0, 601), random.randrange(1, 4),random.randrange(-4, 0), arcade.color.RED)
            self.list.append(self.snowflake)
    def on_draw(self):
        arcade.start_render()
        for i in self.list:
            i.draw_snowflake()
        arcade.draw_rectangle_filled(300, 300, 10, 600, arcade.color.RED_BROWN)
        arcade.draw_rectangle_filled(300, 300, 600, 10, arcade.color.RED_BROWN)
    def on_update(self, dt):
        for i in self.list:
            i.update_snowflake()
def main():
    window = Snowfall(600, 600, "Snowfall")
    arcade.run()

main()