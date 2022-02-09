import arcade

SW = 640
SH = 480

class Balls():
    def __init__(self, pos_x, pos_y, dx, dy, rad, c):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.c = c
    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.c)
    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        #bounce balls of walls
        if self.pos_x > SW-self.rad or self.pos_x < self.rad:
            self.dx *= -1
        if self.pos_y > SW-self.rad or self.pos_y < self.rad:
            self.dy *= -1




class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.ball = Balls(320, 240, 3, 2, 15, arcade.color.FRENCH_PUCE)
    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()
    def on_update(self, dt):
        self.x += 1
        self.y -= 1



def myprogram():
    Window = MyGame(SW, SH, "Windows 10")
    arcade.run()

if __name__ == "__main__":
    myprogram()