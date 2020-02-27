'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.
'''
import arcade

class snow_ball:
    print()

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
    def on_draw(self):
        arcade.start_render()

def main():
    SH = 600
    SW = 600
    window = MyGame(SH,SW, "SnowFall")
    arcade.run()

main()
