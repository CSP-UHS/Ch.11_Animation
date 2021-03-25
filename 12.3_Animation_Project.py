'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade

SW = 800
SH = 600
bird_count = 0


class Bird:
    def __init__(self, x, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.c = c

    def draw_bird(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_bird(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < self.r or self.x >= SW - self.r:
            self.dx *= -1
        if self.y < self.r or self.y >= SH - self.r:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BURLYWOOD)
        self.bird = Bird(320.5, 240, 5, -2, 30, arcade.color.MISTY_ROSE)

    def on_draw(self):
        arcade.start_render()
        self.bird.draw_bird()
        # draws sea & lighthouse
        arcade.draw_rectangle_filled(screen_width / 2, screen_height / 6, screen_width - 1, screen_height / 3,
                                     (52, 143, 171))
        arcade.draw_rectangle_filled(100, 0, 150, 800, arcade.color.ASH_GREY)
        arcade.draw_rectangle_filled(100, 100, 50, 50, arcade.color.BLACK)
        arcade.draw_rectangle_filled(100, 300, 50, 50, arcade.color.BLACK)
        arcade.draw_rectangle_filled(100, 400, 200, 50, arcade.color.ASH_GREY)
        arcade.draw_triangle_filled(30, 425, 170, 425, 105, 525, arcade.color.AMERICAN_ROSE)
        arcade.draw_circle_filled(105, 525, 10, (247, 244, 213))

    def on_update(self, dt):
        self.bird.update_bird()


def main():
    window = MyGame(SW, SH, "My Game")
    arcade.run()




# draws birds
def draw_bird(x, y):
    arcade.draw_arc_outline(x, y, 20, 20, arcade.color.BLACK, 0, 90)
    arcade.draw_arc_outline(x + 20, y, 20, 20, arcade.color.BLACK, 90, 180)


if __name__ == "__main__":
    main()
