"""
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
"""
import arcade
import random

SW = 600
SH = 600
box_num = 30
BW = 30


class Box:
    def __init__(self, x, y, side, dx, dy, c):
        self.x = x
        self.y = y
        self.side = side
        self.dx = dx
        self.dy = dy
        self.c = c

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off left
        if self.x <= BW + self.side / 2:
            self.dx *= -1
            self.c = arcade.color.PINK
        # Bounce off right
        if self.x >= SW - BW - self.side / 2:
            self.dx *= -1
            self.c = arcade.color.BANANA_YELLOW
        # Bounce off top
        if self.y >= SH - BW - self.side / 2:
            self.dy *= -1
            self.c = arcade.color.BLUE_GREEN
        # Bounce off bottom
        if self.y <= BW + self.side / 2:
            self.dy *= -1
            self.c = arcade.color.BLUEBERRY


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.box_list = []  # Make list to hold boxes

        # create boxes
        for i in range(box_num):
            s = random.randint(10, 50)
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            x = random.randint(BW + s // 2, SW - BW - s // 2)
            y = random.randint(BW + s // 2, SW - BW - s // 2)
            c = arcade.color.BLACK
            if dx == 0 and dy == 0:
                dx = 20
            box = Box(x, y, s, dx, dy, c)
            self.box_list.append(box)

    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.draw_box()
        # Make rails
        arcade.draw_rectangle_filled(BW // 2, SH // 2, BW, SH, arcade.color.PINK)  # Left
        arcade.draw_rectangle_filled(SW - BW // 2, SH // 2, BW, SH, arcade.color.BANANA_YELLOW)  # Right
        arcade.draw_rectangle_filled(SW // 2, SH - BW // 2, SW, BW, arcade.color.BLUE_GREEN)  # Top
        arcade.draw_rectangle_filled(SW // 2, BW // 2, SW, BW, arcade.color.BLUEBERRY)  # Bottom

    def on_update(self, dt):
        for box in self.box_list:
            box.update_box()


def main():
    window = MyGame(SW, SH, "30 Boxes")
    arcade.run()


if __name__ == "__main__":
    main()
