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

pallete = ["dd4444", "f48080", "2d676f", "194b4f", "ffdcdc"]



# class Arrow:
#     def __init__(self, fx, fy, sy, sx, tx, ty, cor):
#         self.fx = fx
#         self.sx = sx
#         self.tx = tx
#
#         self.fy = fy
#         self.sy = sy
#         self.ty = ty
#         self.cor = cor
#
#     def draw_arrow(self):
#         arcade.draw_triangle_filled(self.fx, self.fy + 300, self.sx, self.sy + 300, self.tx, self.ty + 300, self.cor)
#         arcade.draw_text("PAUSED", SW/2, SH*7/8, arcade.color.WHITE, font_size=25, anchor_x="center")
#
#     def update_arrow(self, dt, velocity):
#         while self.sy > -100:
#             self.fy -= velocity*dt
#             self.sy -= velocity*dt
#             self.ty -= velocity*dt
#
#     def reset_arrow(self, dt, velocity):
#         while self.sy < -100:
#             self.fy += velocity*dt
#             self.sy += velocity*dt
#             self.ty += velocity*dt
class Box:
    def __init__(self, pos_x, pos_y, dx, dy, w, h, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.w = w
        self.h = h
        self.color = color

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.w, self.h, self.color)

    def update_box(self, dt):
        # bounces box off edge of bars and changes color
        if self.pos_x + round(self.w/2) + 30 >= SW:
            self.dx *= -1
            self.color = arcade.color_from_hex_string(pallete[3])
        if self.pos_x < round(self.w/2) + 30:
            self.dx *= -1
            self.color = arcade.color_from_hex_string(pallete[2])

        if self.pos_y + round(self.h/2) >= SH - 30:
            self.dy *= -1
            self.color = arcade.color_from_hex_string(pallete[0])
        if self.pos_y - round(self.h/2) <= 0 + 30:
            self.dy *= -1
            self.color = arcade.color_from_hex_string(pallete[1])

        self.pos_x += self.dx * dt
        self.pos_y += self.dy * dt


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.timeScale = 1
        self.timeScaleD = 0.0275

        self.boxes = []
        for i in range(30):
            w = random.randint(10, 50)
            h = w
            x = random.randint(w+30, SW-w-30)
            y = random.randint(w+30, SH-w-30)
            vx = random.randint(-5, 5)
            while vx == 0:
                vx = random.randint(-5, 5)
            vy = random.randint(-5, 5)
            while vy == 0:
                vy = random.randint(-5, 5)
            c = arcade.color.BLACK
            self.box = Box(x, y, vx, vy, w, h, c)
            self.boxes.append(self.box)

        # self.arrows = []
        # fx = SW / 3
        # sx = SW / 3
        # tx = SW * 2/3
        #
        # fy = SH * 2 / 3
        # sy = SH / 3
        # ty = SH / 2
        # cor = arcade.color.WHITE
        # self.arrow = Arrow(fx, fy, sx, sy, tx, ty, cor)
        # self.arrows.append(self.arrow)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color_from_hex_string(pallete[4]))

        arcade.draw_rectangle_filled(SW / 2, SH - 15, SW, 30, arcade.color_from_hex_string(pallete[0]))
        arcade.draw_rectangle_filled(SW / 2, 15, SW, 30, arcade.color_from_hex_string(pallete[1]))

        arcade.draw_rectangle_filled(15, SH / 2, 30, SH, arcade.color_from_hex_string(pallete[2]))
        arcade.draw_rectangle_filled(SW - 15, SH / 2, 30, SH, arcade.color_from_hex_string(pallete[3]))
        for box in self.boxes:
            box.draw_box()
        # for arrow in self.arrows:
        #     arrow.draw_arrow()

    def on_update(self, dt):
        self.timeScale = max(min(self.timeScale + self.timeScaleD, 1), 0)
        for box in self.boxes:
            box.update_box(self.timeScale)

    def on_key_press(self, key, mod):
        if key == arcade.key.SPACE:
            self.timeScaleD *= -1
            # v = 10
            # for arrow in self.arrows:
            #     if arrow.sy > 100:
            #         arrow.update_arrow(self.timeScale, v)
            #     else:
            #         arrow.reset_arrow(self.timescale, v)


def main():
    MyGame(SW, SH, "30 Boxes")
    arcade.run()


if __name__ == "__main__":
    main()
