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
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col


    def draw_snow(self):
        arcade.draw_line(300, 0, 300, 600, arcade.color.MAHOGANY, 10)
        arcade.draw_line(0, 300, 600, 300, arcade.color.MAHOGANY, 10)
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)


    def update_snow(self):
        self.pos_y += self.dy
        if self.pos_y == 0:
            self.pos_y = 600
        if self.dy == 0:
            self.dy -= 1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowfks = []

        for i in range(300):
            rad = random.randint(1, 3)
            x = random.randint(0, 600)
            y = random.randint(0, 600)
            dx = 0
            dy = random.randint(-4, -1)
            c = arcade.color.WHITE

            snow = Snow(x, y, dx, dy, rad, c)

            self.snowfks.append(snow)

    def on_draw(self):
        arcade.start_render()





        for snow in self.snowfks:
            snow.draw_snow()



    def on_update(self, dt):
        for snow in self.snowfks:
            snow.update_snow()






def myprogram():
    window = MyGame(SW, SH, "Snowfall")
    arcade.run()


if __name__ == "__main__":
    myprogram()
