'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random

SW = 800
SH = 400

class Box:
    def __init__(self, x, y, s, dy, c):
        self.x = x
        self.y = y
        self.s = s
        self.dy = dy
        self.c = c


    def jump(self):
        #if guy in within certan range of "spike" jump
        self.dy = self.dy + 10


    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.s, self.s, self.c)

    def update_box(self):
        self.dy = self.dy -(9.81 / 60)
        self.y = self.y - self.dy




        if self.y < 20:
            self.dy = 0
            self.y = 20

class OogaBooga(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)


    def on_draw(self):
        arcade.start_render()

    def on_update(self, dt):


def main():
    window = Box(30,30,10,0,arcade.color.BLUE)
    arcade.run()


if __name__ == "__main__":
    main()
