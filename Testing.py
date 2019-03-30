import arcade
import random

SW = 640
SH = 480


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.x=random.randrange(0,480)
        self.y=random.randrange(0,480)

    def on_draw(self): # Draws the ball
        arcade.start_render()
        arcade.draw_circle_filled(self.x, self.y, 15, arcade.color.AUBURN)

    def on_update(self, dt):
        self.x += 0
        self.y += -3 # Moves the circle down

        if self.y >= 480:
            self.y = -20
        elif self.y <= 0:
            self.y = 480


def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()


main()