"""
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

DONE 1.) Screen size 600 x 600
DONE 2.) Draw four 30px wide side rails on all four sides of the window
DONE 3.) Make each side rail a different color.
DONE 4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
DONE 5.) Animate them starting at random speeds from -300 to +300 pixels/second.
DONE 6.) All boxes must be moving.
DONE 7.) Start all boxes in random positions between the rails.
DONE 8.) Bounce boxes off of the side rails when the box edge hits the side rail.
DONE 9.) When the box bounces change its color to the rail it just hit.
DONE 10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
"""
import arcade
import random
SW = 600
SH = 600


class Box():
    def __init__(self, xx, yy, width, height, dx, dy, color):  # dx and dy are similar to velocities
        self.xx = xx
        self.yy = yy
        self.w = width
        self.h = height
        self.dx = dx
        self.dy = dy
        self.color = color

    def draw_box(self):
        # Squares (not moving yet)
        arcade.draw_rectangle_filled(self.xx, self.yy, self.w, self.h, self.color)
        # Rectangle Borders
        arcade.draw_rectangle_filled(15, SH / 2, 30, SH - 60, (233, 111, 253))  # left
        arcade.draw_rectangle_filled(SW/2, SH-15, 30, SH - 60, (28, 219, 212), 90)  # Top
        arcade.draw_rectangle_filled(SW-15, SH / 2, 30, SH - 60, (255, 129, 177))  # Right
        arcade.draw_rectangle_filled(SW/2, 15, 30, SH - 60, (255, 161, 0), 90)  # Bottom


    def update_box(self):
        self.xx += self.dx
        self.yy += self.dy
        # Bounce off the sides of the screen

        if self.xx <= 45 or self.xx >= SW - 45:
            self.dx *= -1
            if self.xx <= 45:  # left
                self.color = (233, 111, 253)
            else:  # right
                self.color = (255, 129, 177)
        if self.yy <= 45 or self.yy >= SW - 45:
            self.dy *= -1
            if self.yy >= SW - 45:  # top
                self.color = (28, 219, 212)
            else:  # bottom
                self.color = (255, 161, 0)



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.box_list = []
        for i in range(30):
            x = random.randint(50, SW-50)
            y = random.randint(50, SW-50)
            wh = random.randint(10, 50)
            vx = random.randint(-5, 5)
            if vx == 0:
                vx = -1
            vy = random.randint(-5, 5)
            if vy == 0:
                vy = 2
            else:
                pass
            self.box = Box(x, y, wh, wh, vx, vy, arcade.color.BLACK)
            self.box_list.append(self.box)



    def on_draw(self):
        arcade.start_render()
        for item in self.box_list:
            item.draw_box()

    def on_update(self, dt):  # dt = __/60th <-- updating the screen 60 times a second
        self.box.update_box()
        for item in self.box_list:
            item.update_box()


def main():
    window = MyGame(SW, SH, "30 Boxes")
    arcade.run()


if __name__ == "__main__":
    main()
