import arcade

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = "IDK"


class Circle:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw_circle(self):
        arcade.draw_circle_filled(self.x, self.y, 20, arcade.color.WHITE)


def on_draw(dt):
    arcade.start_render()
    circle = Circle()


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()
    circle_list = []
    for i in range(50):
        circle.x =
    arcade.close_window()


if __name__ == "__main__":
    main()
