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

sw = 600
sh = 600
FN = 300

class Flake:
    def __init__(self, x, y, dy, r, c):
        self.x = x
        self.y = y
        self.dy = dy
        self.r = r
        self.c = c

    def draw_flake(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_flake(self):
        self.y += self.dy

#  re-spond flake on the top
        if self.y <= -self.r:
            self.y = random.randint(sh, sh+100)
            self.x = random.randint(0, sw)


class MyGame(arcade.Window):
    def __init__(self, sw, sh, title):
        super().__init__(sw, sh, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.flakelist = []    #  hold all snow flake
        #   create flake
        for i in range(FN):
            r = random.randint(1, 4)
            dy = random.randint(-4, -1)
            x = random.randint(0, sw)
            y = random.randint(0, sh)

            if i == 0:
                c = arcade.color.RED
            else:
                c = arcade.color.WHITE
            make_flake = Flake(x, y, dy, r, c)
            self.flakelist.append(make_flake)


    def on_draw(self):
        arcade.start_render()
        for flake in self.flakelist:
            flake.draw_flake()
        arcade.draw_rectangle_filled(sw//2, sh//2, 10, sh, arcade.color.ALLOY_ORANGE)
        arcade.draw_rectangle_filled(sw//2, sh//2, sw, 10, arcade.color.ALLOY_ORANGE)


    def on_update(self, dt):
        for flake in self.flakelist:
            flake.update_flake()


def main():
    my_window = MyGame(sw, sh, "Snow Fall")

    arcade.run()


if __name__ == "__main__":
    main()