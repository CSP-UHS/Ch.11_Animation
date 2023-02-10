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

SH = 600
SW = 600


class Box:
    def __init__(self, pos_x, pos_y, dx, dy, size, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.col = col

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.size, self.size, self.col)

    def update_box(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        # Bounce ball off of walls
        if self.pos_x > SW - self.size/2 - 30:
            self.dx *= -1
            self.col = arcade.color.UFO_GREEN
        if self.pos_x < 30 + self.size/2:
            self.dx *= -1
            self.col = arcade.color.ALLOY_ORANGE
        if self.pos_y > SH - self.size/2 - 30:
            self.dy *= -1
            self.col = arcade.color.AO
        if self.pos_y < 30 + self.size/2:
            self.dy *= -1
            self.col = arcade.color.RADICAL_RED


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BRIGHT_NAVY_BLUE)
        self.balls = []
        for i in range(30):
            size = random.randint(10, 50)
            x = random.randint(30 + size, 570 - size)
            y = random.randint(30 + size, 570 - size)
            dx = random.randint(-5, 5)
            if dx == 0:
                dx += 1
            dy = random.randint(-5, 5)
            if dy == 0:
                dy += 1
            col = arcade.color.BLACK
            box = Box(x, y, dx, dy, size, col)
            self.balls.append(box)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(300, 585, 540, 30, arcade.color.AO)
        arcade.draw_rectangle_filled(585, 300, 30, 540, arcade.color.UFO_GREEN)
        arcade.draw_rectangle_filled(300, 15, 540, 30, arcade.color.RADICAL_RED)
        arcade.draw_rectangle_filled(15, 300, 30, 540, arcade.color.ALLOY_ORANGE)
        for box in self.balls:
            box.draw_box()

    def on_update(self, dt):
        for box in self.balls:
            box.update_box()


def main():
    window = MyGame(SW, SH, "Thirty Boxes")
    arcade.run()


if __name__ == "__main__":
    main()