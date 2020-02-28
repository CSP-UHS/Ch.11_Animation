'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.
'''
import arcade
import random

class snow_ball:
    def __init__(self, pos_x, pos_y, dy, col):
        self.radius = random.randint(1, 3)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.col = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.col)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.CATALINA_BLUE)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrtb_rectangle_filled(0,600,200,0, arcade.color.AO) # GRASS
        arcade.draw_triangle_filled(100, 200, 300, 400, 500, 200, arcade.color.EBONY) #middle mountian
        arcade.draw_triangle_filled(400, 200, 600, 350, 600, 200, arcade.color.DARK_GRAY)  # right mountian
        arcade.draw_triangle_filled(0,200, 0, 400, 500, 200, arcade.color.DIM_GRAY) #left mountian


def main():
    SH = 600
    SW = 600
    window = MyGame(SH,SW, "SnowFall")
    arcade.run()

main()
