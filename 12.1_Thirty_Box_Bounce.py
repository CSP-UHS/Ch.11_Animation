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
screen_width = 600
screen_height = 600
boxes = 100
wall_collors = [(random.randint(0,255), random.randint(0,255), random.randint(0,255)) # Randomly creates top color
    , (random.randint(0,255), random.randint(0,255), random.randint(0,255)) # Randomly creates bottom color
    , (random.randint(0,255), random.randint(0,255), random.randint(0,255)) # Randomly creates left
    , (random.randint(0,255), random.randint(0,255), random.randint(0,255))] # Right


class Box:
    def __init__(self, x, y, side, speedx, speedy):
        self.x = x
        self.y = y
        self.wx = side
        self.wy = side
        self.color = arcade.color.WHITE
        self.speedx = speedx
        self.speedy = speedy

    def box_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.wx, self.wy, self.color)

    def update_box(self):
        if self.x - 0.5*self.wx <= 30:
            self.speedx = -self.speedx
            self.color = wall_collors[2]
        if self.x + 0.5 * self.wx >= screen_width - 30:
            self.speedx = -self.speedx
            self.color = wall_collors[3]
        if self.y - 0.5*self.wy <= 30:
            self.speedy = -self.speedy
            self.color = wall_collors[1]
        if self.y + 0.5 * self.wy >= screen_height - 30:
            self.speedy = -self.speedy
            self.color = wall_collors[0]
        self.x += self.speedx
        self.y += self.speedy


class Render(arcade.Window):
    def __init__(self, sc_width, sc_height, sc_title):
        super().__init__(sc_width, sc_height, sc_title)
        arcade.set_background_color(arcade.color.BLACK)
        self.box_list = []
        for i in range(boxes):
            spd_x, spd_y = random.randint(-5, 5), random.randint(-5, 5)
            if spd_x == 0 or spd_y == 0:
                i -= 1
                continue
            self.box_list.append(Box(random.randint(60, 480), random.randint(60, 480), random.randint(10, 50), spd_x, spd_y))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(300, 600, 600, 60, wall_collors[0])
        arcade.draw_rectangle_filled(600, 300, 60, 600, wall_collors[3])
        arcade.draw_rectangle_filled(300, 0, 600, 60, wall_collors[1])
        arcade.draw_rectangle_filled(0, 300, 60, 600, wall_collors[2])
        arcade.draw_rectangle_filled(0, 600, 600, 60, wall_collors[0])
        for box in self.box_list:
            box.box_draw()

    def on_update(self, delta_time: float):
        for box in self.box_list:
            box.update_box()


def main():
    Render(screen_width, screen_height, "Thirty Boxes")
    arcade.run()


if __name__ == "__main__":
    main()
