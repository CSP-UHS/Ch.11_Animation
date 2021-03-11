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
snowflakes = 100


class Circle():
    def __init__(self, x, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.color = c

    def reverse(self):
        # print("woah")
        self.dy = self.dy * -1

    def push(self, cx, x, y):
        if abs(self.x - x) <= 40 and abs(self.y - y) <= 40:
            self.dx = self.dx + cx

    def hold(self, x, y, dx, dy):
        if abs(self.x - x) <= 40 and abs(self.y - y) <= 40:
            self.x = self.x + dx
            self.y = self.y + dy
            self.y = self.y + self.dy

    def drawcircle(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.color)

    def updatecirlce(self):
        self.dx = (self.dx + (random.randint(-1, 1)) * 0.2)
        if abs(self.dx) > 3:
            self.dx = self.dx * 0.5
        self.x += self.dx
        self.y += self.dy

        if self.y <= 0:
            self.y = random.randint(600, 700)
        if self.y >= 701:
            self.y = random.randint(-100, 0)
        if self.x > 604:
            self.x = -4
        if self.x < -4:
            self.x = 604


class MyGame(arcade.Window):
    def __init__(self, width, height, title, boxnum):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        pos = 0
        self.flake_list = []
        for i in range(snowflakes):
            pos += 1
            if pos == 1:
                self.circle = Circle(random.randint(0, 600), random.randint(0, 600), 0, (-1 * random.randint(1, 4)),
                                     random.randint(1, 3), arcade.color.RED)
            else:
                self.circle = Circle(random.randint(0, 600), random.randint(0, 600), 0, (-1 * random.randint(1, 4)),
                                     random.randint(1, 3), arcade.color.WHITE)
            self.flake_list.append(self.circle)

    def on_draw(self):
        arcade.start_render()
        for flake in self.flake_list:
            flake.drawcircle()

        arcade.draw_rectangle_filled(300, 300, 600, 20, arcade.color.BROWN)
        arcade.draw_rectangle_filled(300, 300, 20, 600, arcade.color.BROWN)

    def on_update(self, dt):
        for box in self.flake_list:
            box.updatecirlce()

    def on_key_press(self, r: int, modifiers: int):
        print("reverse")
        for flake in self.flake_list:
            flake.reverse()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        for flake in self.flake_list:
            flake.push(dy, x, y)

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        for flake in self.flake_list:
            flake.hold(x, y, dx, dy)


def main():
    mywindow = MyGame(SW, SH, "Snowfall", snowflakes)
    arcade.run()


if __name__ == "__main__":
    main()
