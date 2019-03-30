import arcade
SW = 1280
SH = 720


class Rectangle:
    def __init__(self, pos_x, pos_y, width, height, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.col = col

    def draw_rectangle(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.height, self.width, self.col)

    def update_rectangle(self):
        pass


class Ball:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_ball(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        # bounce off edge of screen
        if self.pos_x < self.rad or self.pos_x > SW - self.rad:
            self.dx *= -1
        if self.pos_y < self.rad or self.pos_y > SH - self.rad:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ANTIQUE_WHITE)
        self.rectangle = Rectangle(200, 360, 720, 400, arcade.color.YELLOW)
        self.ball = Ball(740, 240, 3, 2, 50, arcade.color.SNOW)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()
        self.rectangle.draw_rectangle()

    def on_update(self, dt):
        self.ball.update_ball()
        self.rectangle.update_rectangle()


def main():
    window = MyGame(SW, SH, "Drawing Example")
    arcade.run()


main()