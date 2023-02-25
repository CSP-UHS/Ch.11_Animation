"""
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.
"""
import arcade
import random
SW = 600
SH = 600


class Image():
    def __init__(self, xx, yy, dx, dy, radius, color):  # dx and dy are similar to velocities
        self.xx = xx
        self.yy = yy
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def draw_house(self):
        # sun (moving object)
        arcade.draw_circle_filled(self.xx, self.yy, self.radius, self.color)
        # land
        arcade.draw_ellipse_filled(300, 10, 600, 300, (0, 255, 0))
        # Chimney
        arcade.draw_rectangle_filled(420, 350, 60, 120, arcade.color.BRICK_RED)
        arcade.draw_rectangle_outline(420, 350, 60, 120, arcade.color.BLACK)
        # polygon for the house (pentagon)
        point_list = ((100, 80), (100, 280), (300, 430), (500, 280), (500, 80))
        arcade.draw_polygon_filled(point_list, arcade.color.GRAY)
        arcade.draw_polygon_outline(point_list, (0, 0, 0))
        # door rectangle
        arcade.draw_rectangle_filled(300, 150, 80, 140, arcade.color.BROWN_NOSE)
        # window rectangle
        arcade.draw_rectangle_filled(180, 200, 80, 80, arcade.color.LIGHT_BLUE)
        arcade.draw_rectangle_outline(180, 200, 80, 80, arcade.color.BLACK)
        arcade.draw_rectangle_filled(420, 200, 80, 80, arcade.color.LIGHT_BLUE)
        arcade.draw_rectangle_outline(420, 200, 80, 80, arcade.color.BLACK)
        # roof
        arcade.draw_line(90, 280, 316, 434, (0, 0, 0), 20)
        arcade.draw_line(510, 280, 312, 424, (0, 0, 0), 20)

    def update_image(self):
        self.xx += self.dx
        self.yy += self.dy
        if self.yy >= 530:
            self.dx *= 0.7
            self.dy *= -0.7



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        y = 240
        if y <= 500:
            x = arcade.color.LIGHT_BLUE
        else:
            x = arcade.color.BLACK
            self.yy += 20
        arcade.set_background_color(x)
        self.ball_list = []
        self.ball = Image(10, y, 1, 1, 20, arcade.color.YELLOW)
        self.ball_list.append(self.ball)


    def on_draw(self):
        arcade.start_render()
        for item in self.ball_list:
            item.draw_house()

    def on_update(self, dt):  # dt = __/60th <-- updating the screen 60 times a second
        self.ball.update_image()
        for item in self.ball_list:
            item.update_image()


def main():
    window = MyGame(SW, SH, "Hello!")
    arcade.run()


if __name__ == "__main__":
    main()
