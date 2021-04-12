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

sw = 600
sh = 600

box_num = 30
bw = 30

class Box:
    def __init__(self, x, y, side, dx, dy, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.side = side
        self.c = c

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

#  bounce off left
        if self.x <= bw + self.side/2:
            self.dx *= -1
            self.c = arcade.color.RED
            #  right
        if self.x >= sw - bw - self.side/2:
            self.dx *= -1
            self.c = arcade.color.YELLOW
        #  top
        if self.y >= sh - bw - self.side/2:
            self.dy *= -1
            self.c = arcade.color.GREEN
        #  bottom
        if self.y <= bw + self.side/2:
            self.dy *= -1
            self.c = arcade.color.BLUE



class MyGame(arcade.Window):
    def __init__(self, sw, sh, title):
        super().__init__(sw, sh, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.boxlist = []   #  hold all boxes
        for i in range(box_num):
            s = random.randint(10, 50)
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            x = random.randint(bw+s//2, sw-bw-s//2)
            y = random.randint(bw+s//2, sh-bw-s//2)
            c = arcade.color.BLACK
            if dx == 0 and dy == 0:
                dx = 20

            box = Box(x, y, s, dx, dy, c)
            self.boxlist.append(box)


    def on_draw(self):
        arcade.start_render()
        for box in self.boxlist:
            box.draw_box()
        arcade.draw_rectangle_filled(bw//2, sh//2, bw, sh, arcade.color.RED)
        arcade.draw_rectangle_filled(sw-bw//2, sh//2, bw, sh, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(sw//2, sh-bw//2, sw, bw, arcade.color.GREEN)
        arcade.draw_rectangle_filled(sw//2, bw//2, sw, bw, arcade.color.BLUE)


    def on_update(self, dt):
        for box in self.boxlist:
            box.update_box()


def main():
    my_window = MyGame(sw, sh, "30 boxes")

    arcade.run()


if __name__ == "__main__":
    main()


