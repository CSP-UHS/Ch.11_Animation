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
SF = 300


class Flake:
    def __init__(self, x_pos, y_pos, dy, rad, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dy = dy
        self.rad = rad
        self.color = color

    def draw_flake(self):
        arcade.draw_circle_filled(self.x_pos, self.y_pos, self.rad, self.color)

    def update_flake(self):
        self.y_pos += self.dy

        #Bouncing the flakes off of the edges
        if self.y_pos < 0:
            self.x_pos = random.randint(0, SW)
            self.y_pos = random.randint(SH, SH + 50)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.flake_list = []
        for i in range(SF):
            dy = random.randint(-4, -1)
            rad = random.randint(1, 3)
            x = random.randint(0, SW)
            y = random.randint(0, SH)
            if i == 0:
                color = arcade.color.RED_DEVIL
            else:
                color = arcade.color.WHITE
            flake = Flake(x, y, dy, rad, color)
            self.flake_list.append(flake)

    def on_draw(self):
        arcade.start_render()
        for flake in self.flake_list:
            flake.draw_flake()
        arcade.draw_rectangle_filled(SW/2, SH/2, 10, SH, arcade.color.RED_BROWN)
        arcade.draw_rectangle_filled(SW / 2, SH / 2, SW, 10, arcade.color.RED_BROWN)
    def on_update(self, dt):
        for flake in self.flake_list:
            flake.update_flake()

def main():
    window = MyGame(SW, SH, "Snowfall",)
    arcade.run()

if __name__=="__main__":
    main()