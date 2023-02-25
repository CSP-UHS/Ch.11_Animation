"""
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

DONE 1.) Create a 600 x 600 window with black background
DONE 2.) Window title equals "Snowfall"
DONE 3.) Crossbars 10 px wide. Snow must be outside!
DONE 4.) Make snowflake radius random between 1-3
DONE 5.) Randomly start snowflakes anywhere in the window.
DONE 6.) Random downward speed of -4 to -1
DONE 7.) Start snowflakes again at random x from 0-600 and random y from 600-700
DONE 8.) Generate 300 snowflakes
DONE 9.) Color snowflake #1 red just for fun.
DONE 10.) All other snowflakes should be white.

"""
import arcade
import random
SW = 600
SH = 600


class Ball():
    def __init__(self, xx, yy, dy, radius, color):  # dx and dy are similar to velocities
        self.xx = xx
        self.yy = yy
        self.dy = dy
        self.radius = radius
        self.color = color

    def draw_ball(self):
        arcade.draw_rectangle_filled(SW / 2, SH / 2, 10, SH*2, (180, 97, 33))
        arcade.draw_rectangle_filled(SW / 2, SH / 2, 10, SW * 2, (180, 97, 33), 90)
        arcade.draw_circle_filled(self.xx, self.yy, self.radius, self.color)

    def update_ball(self):
        self.yy += self.dy
        # when balls get to the bottom, put them back at the top
        if self.yy <= 0:
            self.yy = SH+10


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball_list = []
        for i in range(300):
            x = random.randint(0, 600)
            y = random.randint(600, 700)
            vy = random.randint(-4, -1)
            rad = random.randint(1, 3)
            if i == 1:
                c = (255, 0, 0)
            else:
                c = (255, 255, 255)
            self.ball = Ball(x, y, vy, rad, c)
            self.ball_list.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        for item in self.ball_list:
            item.draw_ball()

    def on_update(self, dt):  # dt = __/60th <-- updating the screen 60 times a second
        for item in self.ball_list:
            item.update_ball()


def main():
    window = MyGame(SW, SH, "SNOWFALL!")
    arcade.run()


if __name__ == "__main__":
    main()
