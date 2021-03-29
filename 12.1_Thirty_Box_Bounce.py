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
box_num = 200


class Box:
    def __init__(self, x, y, w, h, dx, dy, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.w = w
        self.h = h
        self.dy = dy
        self.c = c

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.w, self.h, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= (self.w / 2) + 30 or self.x >= SW - (self.w / 2) - 30:
            self.dx *= -1
        if self.y <= (self.h / 2) + 30 or self.y >= SH - (self.h / 2) - 30:
            self.dy *= -1
        if self.x <= (self.w / 2) + 30:
            self.c = arcade.color.SKY_BLUE
        if self.x >= SW - (self.w / 2) - 30:
            self.c = arcade.color.ORANGE_PEEL
        if self.y <= (self.h / 2) + 30:
            self.c = arcade.color.BLUE_GREEN
        if self.y >= SH - (self.h / 2) - 30:
            self.c = arcade.color.MAROON


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.box_list = []
        arcade.set_background_color(arcade.color.GHOST_WHITE)
        for i in range(30):
            same_wh = random.randrange(10, 51)
            dx_check = random.randrange(-5, 6)
            dy_check = random.randrange(-5, 6)
            if dx_check == 0 and dy_check == 0:
                dx_check = random.randrange(1, 6)
                dy_check = random.randrange(-5, 0)
            self.box = Box(random.randrange(50, SW - 50 ), random.randrange(50, SH - 50), same_wh, same_wh, dx_check, dy_check,
                           arcade.color.BLACK)
            self.box_list.append(self.box)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0, 30, SH - 30, 30, arcade.color.SKY_BLUE)
        arcade.draw_lrtb_rectangle_filled(30, SW - 30, 30, 0, arcade.color.BLUE_GREEN)
        arcade.draw_lrtb_rectangle_filled(SW - 30, SW, SH - 30, 0, arcade.color.ORANGE_PEEL)
        arcade.draw_lrtb_rectangle_filled(30, SW - 30, SH, SH - 30, arcade.color.MAROON)
        for box in self.box_list:
            box.draw_box()

    def on_update(self, dt):
        for box in self.box_list:
            box.update_box()


def main():
    window = MyGame(SW, SH, "thirty box bounce")
    arcade.run()


if __name__ == "__main__":
    main()
