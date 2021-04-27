'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''

import arcade

SW = 640
SH = 480

class scuffed_dvd:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_dvd(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)
    def update_dvd(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        #bounce off edge of screen
        if self.pos_x < self.rad or self.pos_x > SW - self.rad:
            self.dx *= -1
            self.col = arcade.color.LIME_GREEN

        if self.pos_y < self.rad or self.pos_y > SH - self.rad:
            self.dy *= -1
            self.col = arcade.color.CYAN


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.dvd = scuffed_dvd(320, 240, 3, 2, 20, arcade.color.WHITE)
    def on_draw(self):
        arcade.start_render()
        self.dvd.draw_dvd()
    def on_update(self, dt):
        self.dvd.update_dvd()

def main():
    window = MyGame(SW, SH, "Scuffed DVD Bounce")
    arcade.run()

if __name__=="__main__":
    main()

