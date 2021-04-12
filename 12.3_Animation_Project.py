'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random

sw = 600
sh = 600
FN = 100

class Flake:
    def __init__(self, x, y, dy, r, c):
        self.x = x
        self.y = y
        self.dy = dy
        self.r = r
        self.c = c


    def draw_flake(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_flake(self):
        self.y += self.dy

#  re-spond flake on the top
        if self.y <= -self.r:
            self.y = random.randint(sh, sh+100)
            self.x = random.randint(0, sw)


class MyGame(arcade.Window):
    def __init__(self, sw, sh, title):
        super().__init__(sw, sh, title)
        self.background = None

        self.flakelist = []      #   hold all snow flake
        #   create flake
        for i in range(FN):
            r = random.randint(1, 9)
            dy = random.randint(-4, -1)
            x = random.randint(0, sw)
            y = random.randint(0, sh)

            if i == 0 or i == 3:
                r = 8
                c = arcade.color.RUBY_RED
            else:
                c = arcade.color.SMOKY_BLACK
            make_flake = Flake(x, y, dy, r, c)
            self.flakelist.append(make_flake)
        self.background = arcade.load_texture("space_image.jpg")



    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, sw, sh, self.background)
        for flake in self.flakelist:
            flake.draw_flake()
        arcade.draw_triangle_filled(300, 400, 274, 360, 326, 360, arcade.color.RED)
        arcade.draw_rectangle_filled(300, 260, 50, 200, arcade.color.GRAY)
        arcade.draw_rectangle_filled(300, 194, 4, 60, arcade.color.RED)
        point_list = ((275, 220),
                     (240, 180),
                     (240, 160),
                     (275, 175))
        arcade.draw_polygon_filled(point_list, arcade.color.RED)
        point_list = ((325, 220),
                     (360, 180),
                     (360, 160),
                     (325, 175))
        arcade.draw_polygon_filled(point_list, arcade.color.RED)
        point_list = ((290, 160),
                     (280, 150),
                     (320, 150),
                     (310, 160))
        arcade.draw_polygon_filled(point_list, arcade.color.RED)
        arcade.draw_rectangle_filled(300, 180, 4, 2, arcade.color.BLACK)
        arcade.draw_circle_filled(300, 300, 13, arcade.color.WHITE)
        arcade.draw_circle_filled(300, 300, 10, arcade.color.BLACK)
        arcade.draw_line(275, 240, 325, 240, arcade.color.BLACK)
        arcade.draw_rectangle_outline(300, 360, 50, 2, arcade.color.BLACK)
        arcade.draw_line(287, 380, 313, 380, arcade.color.BLACK)



    def on_update(self, dt):
        for flake in self.flakelist:
            flake.update_flake()




def main():
    my_window = MyGame(sw, sh, "Snow Fall")

    arcade.run()


if __name__ == "__main__":
    main()