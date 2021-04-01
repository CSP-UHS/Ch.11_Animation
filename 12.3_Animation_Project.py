'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random

sw = 600
sh = 600

particle_num = 200
bw = 3
mid_bw = 3
mid_bh = 88

class Bomb:
    def __init__(self, x, y, side, dx, dy, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.side = side
        self.c = c

    def draw_particle(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.c)

    def update_particle(self):
        self.x += self.dx
        self.y += self.dy

# bounce off mid left
#         if self.x <= 260 + self.side/2:
#             self.dx *= -1
            #  right
        # if self.x >= 340 - self.side/2:
        #     self.dx *= -1
        #     self.c = arcade.color.YELLOW
        #  left top
        # if self.y >= 340 - bw//2 - self.side/2:
        #     self.dy *= -1
        #     self.c = arcade.color.GREEN
        #  right top
        # if self.y >= 340 - bw - self.side/2:
        #     self.dy *= -1
        #     self.c = arcade.color.GREEN
        #  bottom
        # if self.y <= 260 + self.side/2:
        #     self.dy *= -1
        #     self.c = arcade.color.BLUE
#  bounce off left
        if self.x <= bw + self.side/2:
            self.dx *= -1
            self.c = arcade.color.RED
            #  right
        if self.x >= sw - bw - self.side/2:
            self.dx *= -1
            self.c = arcade.color.YELLOW
        #  top
        if self.y >= sh - bw - self.side/2:
            self.dy *= -1
            self.c = arcade.color.GREEN
        #  bottom
        if self.y <= bw + self.side/2:
            self.dy *= -1
            self.c = arcade.color.BLUE
        #   bounce off the middle block




class MyGame(arcade.Window):
    def __init__(self, sw, sh, title):
        super().__init__(sw, sh, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.particlelist = []   #  hold all boxes
        for i in range(particle_num):
            s = 10
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            x = 300
            y = 300
            c = arcade.color.BLACK
            if dx == 0 and dy == 0:
                dx = 5


            particle = Bomb(x, y, s, dx, dy, c)
            self.particlelist.append(particle)

    def on_draw(self):
        arcade.start_render()
        for particle in self.particlelist:
            particle.draw_particle()
            #  middle box
        #arcade.draw_rectangle_filled(300, 300, 80, 80, arcade.color.BLACK)
        # left
        arcade.draw_rectangle_filled(260, 300, mid_bw, mid_bh, arcade.color.RED)
        # right
        arcade.draw_rectangle_filled(340, 300, mid_bw, mid_bh, arcade.color.YELLOW)
        # bottom
        arcade.draw_rectangle_filled(300, 260, mid_bh, mid_bw, arcade.color.GREEN)
        # top left
        arcade.draw_rectangle_filled(273, 340, mid_bh//3, mid_bw, arcade.color.BLUE)
        # top right
        arcade.draw_rectangle_filled(327, 340, mid_bh//3, mid_bw, arcade.color.BLUE)
#  the second layer
        arcade.draw_rectangle_filled(bw//2, sh//2, bw, sh, arcade.color.RED)
        arcade.draw_rectangle_filled(sw-bw//2, sh//2, bw, sh, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(sw//2, sh-bw//2, sw, bw, arcade.color.GREEN)
        arcade.draw_rectangle_filled(sw//2, bw//2, sw, bw, arcade.color.BLUE)



    def on_update(self, dt):
        for particle in self.particlelist:
            particle.update_particle()


def main():
    my_window = MyGame(sw, sh, "30 boxes")

    arcade.run()


if __name__ == "__main__":
    main()