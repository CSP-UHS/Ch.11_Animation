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

#CHANGE TO BOX CODE FROM BALL CODE

import arcade
import random
SW = 600
SH = 600


class Box():
    def __init__(self, pos_x, pos_y, dx, dy, width, height, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
        self.col = col

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col)

    def update_box(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
        rad = random.randint(1, 3)
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        dx = 0
        dy = random.randint(-4, -1)
        c = arcade.color.WHITE

        #bounce box off of walls
        if self.pos_x > SW-self.width or self.pos_x < self.width:
            self.dx *= -1
        if self.pos_y > SH - self.height or self.pos_y < self.height:
            self.dy *= -1
        if self.dx == 0:
            self.dx += 1
        if self.dy == 0:
            self.dy += 1

        #box color change
        if self.pos_x > SW-self.width:
            self.col = arcade.color.BLUE
        if self.pos_x < self.width:
            self.col = arcade.color.RED
        if self.pos_y > SH - self.height:
            self.col = arcade.color.GREEN
        if self.pos_y < self.height:
            self.col = arcade.color.YELLOW


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.boxes = []

        for i in range(30):
            wid = random.randint(10, 50)
            hei = wid
            x = random.randint(wid, SW-wid)
            y = random.randint(hei, SH - hei)
            dx = random.randint(-3, 3)
            dy = random.randint(-3, 3)
            c = arcade.color.BLACK

            box = Box(x, y, dx, dy, wid, hei, c)

            self.boxes.append(box)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(0, 0, 600, 0, arcade.color.YELLOW, 30)
        arcade.draw_line(0, 0, 0, 600, arcade.color.RED, 30)
        arcade.draw_line(0, 600, 600, 600, arcade.color.GREEN, 30)
        arcade.draw_line(600, 0, 600, 600, arcade.color.BLUE, 30)

        for box in self.boxes:
            box.draw_box()

    def on_update(self, dt):
        for box in self.boxes:
            box.update_box()




def myprogram():
    window = MyGame(SW, SH, "30 boxes")

    arcade.run()

if __name__ == "__main__":
    myprogram()
