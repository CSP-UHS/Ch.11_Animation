import arcade
import random

screen_width = 1280
screen_height = 720
fall_speed = 3
rotation_speed = 2

class Snow:
    def __init__(self, x, y, width, height, color, angle):
        self.pos_x = x
        self.pos_y = y
        self.height = height
        self.width = width
        self.color = color
        self.angle = angle

    def draw_snow(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.color, self.angle)

    def update_snow(self):
        self.pos_y -= fall_speed
        self.pos_x += 0
        self.angle += rotation_speed

        # Teleports the snow to the top if it reaches the bottom
        if self.pos_y <= screen_height-screen_height-100:
            self.pos_y = screen_height + 10


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.snow = Snow(random.randrange(0,1281), 730, 15, 15, arcade.color.SNOW, 45)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        # Put DRAWING CODE HERE
        self.snow.draw_snow()

    def update(self, dt):
        self.snow.update_snow()


def main():
    MyGame(screen_width, screen_height, "Snowing")
    arcade.run()
main()