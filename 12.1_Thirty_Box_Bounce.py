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
number_of_boxes = 30


class Rectangle:
    def __init__(self, pos_x, pos_y, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw_rectangle(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.color)


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

        # Bounce off edge of screen & Change Color
        if self.pos_x < (self.width/2) + 30:  # Block Left
            self.dx *= -1
            self.color = arcade.color.RED
        if self.pos_x > SW - 30 - self.width/2:  # Block Right
            self.dx *= -1
            self.color = arcade.color.PURPLE
        if self.pos_y < self.height/2 + 30:  # Block Bottom
            self.dy *= -1
            self.color = arcade.color.ORANGE
        if self.pos_y > SH - 30 - self.height/2:  # Block Top
            self.dy *= -1
            self.color = arcade.color.BLUE


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.boxlist=[]
        self.rectanglelist = []
        self.rectanglelist.append(Rectangle(15, 300, 30, 540, arcade.color.RED))  # Left
        self.rectanglelist.append(Rectangle(585, 300, 30, 540, arcade.color.PURPLE))  # Right
        self.rectanglelist.append(Rectangle(300, 15, 540, 30, arcade.color.ORANGE))  # Bottom
        self.rectanglelist.append(Rectangle(300, 585, 540, 30, arcade.color.BLUE))  # Top
        for i in range(number_of_boxes):
            size = random.randrange(10, 50)
            self.box = Box(random.randrange(50, 560), random.randrange(50, 560), random.randrange(-10, 10),
                           random.randrange(-10, 10), size, size, arcade.color.AUBURN)
            self.boxlist.append(self.box)

    def on_draw(self):
        arcade.start_render()
        for self.box in self.boxlist:
            self.box.draw_box()
        for self.rectangle in self.rectanglelist:
            self.rectangle.draw_rectangle()

    def on_update(self, dt):
        for self.box in self.boxlist:
            self.box.update_box()


def main():
    window = MyGame(SW, SH, "30 Boxes")
    arcade.run()


main()