'''
import arcade
import random

SW = 640
SH = 480


class Ball():
    def __init__(self, xx, yy, dx, dy, radius, color):  # dx and dy are similar to velocities
        self.xx = xx
        self.yy = yy
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color

    def draw_ball(self):
        arcade.draw_circle_filled(self.xx, self.yy, self.radius, self.color)


    def update_ball(self):
        self.xx += self.dx
        self.yy += self.dy
        # Bounce off the sides of the screen
        if self.xx < self.radius or self.xx > SW - self.radius:
            self.dx *= -1
        if self.yy < self.radius or self.yy > SH - self.radius:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.RHYTHM)
        self.ball_list = []
        for i in range(50):
            rad = random.randint(10, 30)
            x = random.randint(rad, SW - rad)
            y = random.randint(rad, SH - rad)
            vx = random.randint(-2, 4)
            if vx == 0:
                vx = 1
            vy = random.randint(-2, 4)
            if vy == 0:
                vy = 1
            c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.ball = Ball(x, y, vx, vy, rad, c)
            self.ball_list.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        for item in self.ball_list:
            item.draw_ball()

    def on_update(self, dt):  # dt = __/60th <-- updating the screen 60 times a second
        self.ball.update_ball()
        for item in self.ball_list:
            item.update_ball()



def main():
    window = MyGame(SW, SH, "Hello!")
    arcade.run()


if __name__ == "__main__":
    main()
'''
