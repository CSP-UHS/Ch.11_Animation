'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

(1.) Create a 600 x 600 window with black background
(2.) Window title equals "Snowfall"
(3.) Crossbars 10 px wide. Snow must be outside!
(4.) Make snowflake radius random between 1-3
(5.) Randomly start snowflakes anywhere in the window.
(6.) Random downward speed of -4 to -1
(7.) Start snowflakes again at random x from 0-600 and random y from 600-700
(8.) Generate 300 snowflakes
(9.) Color snowflake #1 red just for fun.
(10.) All other snowflakes should be white.


'''

import arcade
import random

SW = 600
SH = 600
done = False


class Snow:
    def __init__(self, pos_x, pos_y, dy, rad, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.rad = rad
        self.color = color

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.color)

    def update_ball(self):

        # if self.pos_y + self.rad >= SH or self.pos_y - self.rad <= 0:
        #     self.dy *= -1

        self.pos_y += self.dy

        if self.pos_y <= -self.rad:
            self.pos_x = random.randint(0, SW)
            self.pos_y = random.randint(SH, SH + 100)
            self.dy = random.randint(-5, -2)

        if round(SW / 2) - 5 - self.rad < self.pos_x < round(SW / 2) + 5 + self.rad:
            self.pos_x += 10
        if round(SW / 2) - 5 - self.rad < self.pos_y < round(SW / 2) + 5 + self.rad:
            self.pos_y -= 10


class Snowfall(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowflakes = []

        for i in range(0, 350):
            r = random.randint(1, 3)
            x = random.randint(r, SW - r)
            while round(SW/2) - 5 < x < round(SW/2) + 5:
                x = random.randint(r, SW - r)
            y = random.randint(600, 790)
            while round(SW / 2) - 5 < y < round(SW / 2) + 5:
                y = random.randint(r, SH - r)
            vy = random.randint(-5, -2)
            while vy == 0:
                vy = random.randint(-6, -2)
            if i == 1:
                c = arcade.color.RED
            else:
                c = arcade.color.WHITE
            self.snowflake = Snow(x, y, vy, r, c)
            self.snowflakes.append(self.snowflake)

    def on_draw(self):
        arcade.start_render()

        # window
        arcade.draw_rectangle_filled(round(SW / 2), round(SH / 2), 10, SH, arcade.color.COFFEE)
        arcade.draw_rectangle_filled(round(SW / 2), round(SH / 2), SW, 10, arcade.color.COFFEE)

        for snowflake in self.snowflakes:
            snowflake.draw_ball()

    def on_update(self, dt):
        for snowflake in self.snowflakes:
            snowflake.update_ball()


def main():
    Snowfall(SW, SH, "Snowfall")
    arcade.run()


if __name__ == "__main__":
    main()
    