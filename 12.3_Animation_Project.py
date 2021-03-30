'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade

SW = 800
SH = 600


class Ball:
    def __init__(self, x, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.c = c

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_ball(self):
        self.x += self.dx
        self.y += self.dy

        if self.x < self.r or self.x >= SW - self.r:
            self.dx *= -1
        if self.y < self.r or self.y >= SH - self.r:
            self.dy *= -1

    def update_sky(self):
        if self.y < 150:
            arcade.set_background_color(arcade.color.DARK_BLUE)
        elif self.y > 250:
            arcade.set_background_color((173, 216, 230))


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color((173, 216, 230))
        self.ball = Ball(400, 500, 0, -2, 50, arcade.color.YELLOW_ROSE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()
        # draws sea & lighthouse
        arcade.draw_rectangle_filled(SW / 2, SH / 6, SW - 1, SH / 3, (52, 143, 171))
        arcade.draw_rectangle_filled(100, 0, 150, 800, arcade.color.ASH_GREY)
        arcade.draw_rectangle_filled(100, 100, 50, 50, arcade.color.BLACK)
        arcade.draw_rectangle_filled(100, 300, 50, 50, arcade.color.BLACK)
        arcade.draw_rectangle_filled(100, 400, 200, 50, arcade.color.ASH_GREY)
        arcade.draw_triangle_filled(30, 425, 170, 425, 105, 525, arcade.color.AMERICAN_ROSE)
        arcade.draw_circle_filled(105, 525, 10, (247, 244, 213))

    def on_update(self, dt):
        self.ball.update_ball()
        self.ball.update_sky()


def main():
    window = MyGame(SW, SH, "Animation Project - Geni W")
    arcade.run()


if __name__ == "__main__":
    main()
