'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes
'''
import arcade
import random

SW = 600
SH = 600


class Box:
    def __init__(self, pos_x, pos_y, dx, dy, width, height, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
        self.color = color

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.color)

    def update_box(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        # Bounce off edge of screen
        if self.pos_x < self.width/2 or self.pos_x > SW - self.width/2:
            self.dx *= -1
        if self.pos_y < self.height/2 or self.pos_y > SH - self.height/2:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.box = Box(320, 240, 5, 5, 50, 50, arcade.color.AUBURN)

    def on_draw(self):
        arcade.start_render()
        self.box.draw_box()
    def on_update(self, dt):

        self.box.update_box()


def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()

main()