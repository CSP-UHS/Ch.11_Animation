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

class Rectangle:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
    def draw_rectangle(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.rad, self.rad, self.col)
    def update_rectangle(self):
        self.pos_y += self.dy
        self.pos_x += self.dx
        if self.pos_x < 30+self.rad/2:
            self.dx *= -1
            self.col = arcade.color.YELLOW
        if self.pos_x > 570 - self.rad/2:
            self.dx *= -1
            self.col = arcade.color.BLUE
        if self.pos_y < 30+self.rad/2:
            self.dy *= -1
            self.col = arcade.color.GREEN
        if self.pos_y > 570 - self.rad/2:
            self.dy *= -1
            self.col = arcade.color.RED

class ThirtyBoxBounce(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.list = []
        for i in range(30):
            self.rectangle = Rectangle(random.randrange(90,511),random.randrange(90,511), random.randrange(-10,11), random.randrange(-10,11), random.randrange(10,51), arcade.color.BLACK)
            self.list.append(self.rectangle)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, 600, 600, 570, arcade.color.RED)
        arcade.draw_lrtb_rectangle_filled(0, 30, 600, 0, arcade.color.YELLOW)
        arcade.draw_lrtb_rectangle_filled(570, 600, 600, 0, arcade.color.BLUE)
        arcade.draw_lrtb_rectangle_filled(0, 600, 30, 0, arcade.color.GREEN)
        arcade.draw_lrtb_rectangle_filled(0, 30, 600, 570, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(0, 30, 30, 0, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(570, 600, 600, 570, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(570, 600, 30, 0, arcade.color.WHITE)

        for item in self.list:
            item.draw_rectangle()
    def on_update(self, dt):
        for item in self.list:
            item.update_rectangle()
def main():
    window = ThirtyBoxBounce(SW, SH, "30 Boxes")
    arcade.run()

main()