import arcade
import random
SW=640
SH=480

class Ball:
    def __init__(self, pos_x, pos_y,dx,dy,rad,color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad= rad
        self.color = color

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.color)

    def update_ball(self):
        self.pos_x+= self.dx
        self.pos_y+=self.dy
        #Bouncing the ball of of the edges
            # if self.pos_x >SW + self.rad: ####PAC MAN
            #     self.pos_x =- self.rad

        if self.pos_x < self.rad or self.pos_x > SW - self.rad: #Left and Right
            self.dx*=-1
        if self.pos_y < self.rad or self.pos_y > SH - self.rad: #Top and bottom
            self.dy*=-1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        self.ball_list = []
        for i in range(10):
            self.dx = random.randint(-2, 2)
            self.dy = random.randint(-2, 2)
            self.ball= Ball(SW/2, SH/2, self.dx, self.dy, 15, arcade.color.AFRICAN_VIOLET)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()

def main():
    window= MyGame(SW, SH, "Animation")
    arcade.run()
if __name__== "__main__":
    main()