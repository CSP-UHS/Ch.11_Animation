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

SH = 600
SW = 600


class Snowflakes:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_flake(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_flake(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        if self.pos_y < 0:
            self.pos_y += random.randint(600, 700)
            self.dy = random.randint(-4, -1)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.balls = []
        for i in range(300):
            r = random.randint(1, 3)
            x = random.randint(0, SW)
            y = random.randint(600, 700)
            dx = 0
            dy = random.randint(-4, -1)
            if i == 1:
                c = arcade.color.RED
            else:
                c = arcade.color.WHITE
            flake = Snowflakes(x, y, dx, dy, r, c)
            self.balls.append(flake)

    def on_draw(self):
        arcade.start_render()
        for flake in self.balls:
            flake.draw_flake()
        arcade.draw_rectangle_filled(300, 300, 600, 10, arcade.color.BROWN)
        arcade.draw_rectangle_filled(300, 300, 10, 600, arcade.color.BROWN)

    def on_update(self, dt):
        for flake in self.balls:
            flake.update_flake()


def main():
    window = MyGame(SW, SH, "Snowfall")
    arcade.run()


if __name__ == "__main__":
    main()