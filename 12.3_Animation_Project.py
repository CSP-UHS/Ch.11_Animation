'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''

# IMPORTS
import arcade
import random

# VARIABLES
SW = 900
SH = 500



# class MyGame:
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         arcade.set_background_color()
#
#     def on_draw(self):
#         arcade.start_render()
#
# def main():
#     window = MyGame(SW, SH, "Animation Project - Peggy Barley",)
#     arcade.run()
#
# if __name__=="__main__":
#     main()


arcade.open_window(SW, SH, "test")
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()
arcade.draw_rectangle_filled(SW/2, SH/5/2, SW, SH/5, arcade.color.DARK_BROWN)
arcade.draw_rectangle_filled()
# arcade.draw_circle_filled(200, 100, 20, arcade.color.PAPAYA_WHIP)
arcade.finish_render()

arcade.run()
