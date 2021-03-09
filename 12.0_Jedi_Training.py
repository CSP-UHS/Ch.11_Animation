'''
Sign your name:Tom Dau
 
All questions are about the final code in Chapter 12:

1.) Where is the ball's original location?
320, 240
2.) What are the variables dx and dy?
Velocity in pixels
3.) How many pixels/sec does the ball move in the x-direction?
180
4.) How many pixels/sec does the ball move in the y-direction?
-120
5.) Which method is run 60 times/second?
on_update
6.) What does this code do?   self.dx *= -1
Reverses x velocity
7.) What does this code do?  self.pos_y += self.dy
Moves the ball
8.) What is the width of the window?
640
9.) What is this code checking?  self.pos_y > SH - self.rad:
If the ball hit the top border
10.) What is this code checking? if self.pos_x < self.rad
If the ball hit the left border


'''
import arcade

SW = 640
SH = 480


class Ball:
    def __init__(self, x: int, y: int, dx, dy, r, c):
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

        if self.x <= self.r or self.x >= SW - self.r:
            self.dx *= -1

        if self.y <= self.r or self.y >= SH - self.r:
            self.dy *= -1


class OogaBooga(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BYZANTINE)
        self.x = 320
        self.y = 240
        self.r = 15
        self.c = arcade.color.COTTON_CANDY
        self.ball = Ball(320, 240, 3, -2, 15, arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()


def main():
    window = OogaBooga(SW, SH, "Ooga Booga")
    arcade.run()


if __name__ == "__main__":
    main()
