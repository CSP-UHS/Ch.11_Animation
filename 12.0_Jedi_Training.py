'''
Sign your name:__Bawi Thawng__
 
All questions are about the final code in Chapter 12:

1.) Where is the ball's original location?
(320, 240)
2.) What are the variables dx and dy?
valocity
3.) How many pixels/sec does the ball move in the x-direction?
180
4.) How many pixels/sec does the ball move in the y-direction?
-120
5.) Which method is run 60 times/second?
update_ball
6.) What does this code do?   self.dx *= -1
make dx negative and made it go opposite direction.
7.) What does this code do?  self.pos_y += self.dy
move the ball to dy or it add dy to pos_y to move it
8.) What is the width of the window?
640
9.) What is this code checking?  self.pos_y > SH - self.rad:
if the ball radius is touching or crossing the SH
10.) What is this code checking? if self.pos_x < self.rad
check if it hit the left side of the wall



'''
import arcade
import random

sw = 640
sh = 480


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

        if self.x <= self.r or self.x >= sw - self.r:
            self.dx *= -1
        if self.y <= self.r or self.y >= sh - self.r:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, sw, sh, title):
        super().__init__(sw, sh, title)
        arcade.set_background_color(arcade.color.ALMOND)
        self.ball = Ball(320, 240, 3, -2, 15, arcade.color.STAR_COMMAND_BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()


def main():
    my_window = MyGame(sw, sh, "Game")

    arcade.run()


if __name__ == "__main__":
    main()