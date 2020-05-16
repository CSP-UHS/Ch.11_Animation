'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''

import arcade
import random

SW = 600
SH = 600
box_num = 30

class Box:
    def __init__(self, x_pos, y_pos, dx, dy, side, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.dx = dx
        self.dy = dy
        self.side = side
        self.color = color

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x_pos, self.y_pos, self.side, self.side, self.color)

    def update_box(self):
        self.y_pos += self.dy
        self.x_pos += self.dx

        # Bouncing the boxes off left
        if self.x_pos < 30 + self.side/2:
            self.dx *= -1
            self.color = arcade.color.RED

        # Bouncing the boxes off right
        if self.x_pos > SW - 30 - self.side/2:
            self.dx *= -1
            self.color = arcade.color.YELLOW

        # Bouncing the boxes off bottom
        if self.y_pos < 30 + self.side/2:
            self.dy *= -1
            self.color = arcade.color.GREEN

        # Bouncing the boxes off top
        if self.y_pos > SH - 30 - self.side/2:
            self.dy *= -1
            self.color = arcade.color.BLUE

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.box_list = []
        for i in range(box_num):
            dy = random.randint(-5, 5)
            dx = random.randint(-5, 5)
            side = random.randint(10, 50)
            x = random.randrange(30 + int(side/2), SW - 30 - int(side/2))
            y = random.randrange(30 + int(side / 2), SW - 30 - int(side / 2))
            color = arcade.color.BLACK

            if dx == 0 and dy == 0:
                dx = 100
                dy = 100

            box = Box(x, y, dx, dy, side, color)
            self.box_list.append(box)

    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.draw_box()
        # RAILS
        arcade.draw_rectangle_filled(15, SH/2, 30, SH-60, arcade.color.RED)  # LEFT
        arcade.draw_rectangle_filled(SW-15, SH/2, 30, SH-60, arcade.color.YELLOW)  # RIGHT
        arcade.draw_rectangle_filled(SW/2, 15, SW-60, 30, arcade.color.GREEN)  # TOP
        arcade.draw_rectangle_filled(SW/2, SH-15, SW-60, 30, arcade.color.BLUE)  # BOTTOM

    def on_update(self, dt):
        for box in self.box_list:
            box.update_box()

def main():
    window = MyGame(SW, SH, "30 Boxes",)
    arcade.run()

if __name__=="__main__":
    main()