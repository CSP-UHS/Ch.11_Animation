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


class Snowflake:
    def __init__(self, color, y):
        self.radius = random.randint(1, 3)
        self.x = random.randint(0, SW)
        self.y = y
        self.color = color
        self.speed = random.randint(-4, -1)

    def draw_snow(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def snow_update(self):
        self.y += self.speed


class Render(arcade.Window):
    def __init__(self, sc_width, sc_height, sc_title):
        super().__init__(sc_width, sc_height, sc_title)
        arcade.set_background_color((0, 0, 0))
        self.snow_list = []
        self.snow_list.append(Snowflake((255, 0, 0), random.randint(0, SH*2)))
        for i in range(299):
            self.snow_list.append(Snowflake((255, 255, 255), random.randint(0, SH*2)))

    def on_draw(self):
        arcade.start_render()
        for flake in self.snow_list:
            flake.draw_snow()
        arcade.draw_rectangle_filled(300, 300, 10, 600, arcade.color.WOOD_BROWN)
        arcade.draw_rectangle_filled(300, 300, 600, 10, arcade.color.WOOD_BROWN)

    def on_update(self, delta_time: float):
        for flake in self.snow_list:
            if flake.y < 0:
                self.snow_list.remove(flake)
                self.snow_list.append(Snowflake(arcade.color.WHITE, random.randint(SH, SH*2)))
            flake.snow_update()


def main():
    Render(SW, SH, "Snow")
    arcade.run()


if __name__ == "__main__":
    main()
