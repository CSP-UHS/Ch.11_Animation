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


class Flake:
    # Defines the parameters of a snowflake. Physical attributes and motion included.
    def __init__(self, x: int, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.c = c

    # Defines the physical attributes of a snowflake.
    def draw_flake(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    # Defines the motion of a snowflake.
    def update_flake(self):
        self.x += self.dx
        self.y += self.dy

        if self.y <= 0:  # If a snowflake hits the bottom, move to top.
            self.y = 600
        if self.x <= 0:  # If a snowflake hits the left edge, move to the right.
            self.x = 599
        if self.x >= 600:  # If a snowflake hits the right edge, move to the left.
            self.x = 1


class MyGame(arcade.Window):
    # Initializes a window and the objects.
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.flake_list = []
        pos = 0
        color = arcade.color.WHITE
        for i in range(300):
            pos += 1
            if pos == 1:
                color = arcade.color.RED
            else:
                color = arcade.color.WHITE
            self.flake = Flake(random.randrange(0, 601), random.randrange(0, 601), random.randrange(-1, 1),
                               random.randrange(-4, 0), random.randrange(1, 3), color)
            self.flake_list.append(self.flake)
    # For each snowflake in the snowflake storage list, draw it. Draw any physical attributes of the window.
    def on_draw(self):
        arcade.start_render()
        for flake in self.flake_list:
            flake.draw_flake()
        arcade.draw_rectangle_filled(300, 300, 10, 600, arcade.color.BLEU_DE_FRANCE)
        arcade.draw_rectangle_filled(300, 300, 600, 10, arcade.color.BLEU_DE_FRANCE)
    # Manages the movement of the snowflakes
    def on_update(self, dt):
        for flake in self.flake_list:
            flake.update_flake()

# Main program
def main():
    MyGame(SW, SH, "Snowfall") # Creates a window with a given height and width.
    arcade.run()


if __name__ == "__main__":
    main()
