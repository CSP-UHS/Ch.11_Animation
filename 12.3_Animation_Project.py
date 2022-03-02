
import arcade
import random

SW = 600
SH = 600
FN = 300
BW = 15

class Flake:
    def __init__(self, x, y, dy, r, c):
        self.x = x
        self.y = y
        self.dy = dy
        self.rad = r
        self.col = c


    def draw_flake(self):
        arcade.draw_rectangle_filled(55, 55, 80, 40, arcade.color.DARK_GREEN)
        #arcade.draw_rectangle_filled(55, 55, 10, 10, arcade.color.DARK_GREEN)
        arcade.draw_rectangle_filled(self.x, self.y, self.rad, 5, self.col)

        arcade.draw_triangle_filled(self.x, self.y, 20, 30, 40, 50, arcade.color.RED)
    def update_flake(self):
        self.y += self.dy
        if self.x <= -self.rad:
            self.x = random.randint(SW, SW+100)
            self.y = random.randint(0, SW)

class MyGame(arcade.Window):
    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.flakelist = []    #  hold all snow flake
        for i in range(FN):
            r = random.randint(10, 20)
            dy = random.randint(-4, -1)
            x = random.randint(0, SW)
            y = random.randint(0, SH)

            if i == 0:
                c = arcade.color.NAVY_BLUE
            else:
                c = arcade.color.NAVY_BLUE
            make_flake = Flake(x, y, dy, r, c)
            self.flakelist.append(make_flake)

    def on_draw(self):
        arcade.start_render()
        for flake in self.flakelist:
            flake.draw_flake()
        arcade.draw_rectangle_filled(SW, SH//2, 20, SH, arcade.color.GREEN)
        arcade.draw_rectangle_filled(BW//2, SH//2, BW, SH, arcade.color.GREEN)
        arcade.draw_rectangle_filled(SW//2, 3, SW, 25, arcade.color.GREEN)
        arcade.draw_rectangle_filled(SW//2, 600, SW, 25, arcade.color.GREEN) #reverse this
        #arcade.draw_rectangle_filled(SW//2, SH//2, SW, 10, arcade.color.WHITE_SMOKE)

    def on_update(self, dt):
        for flake in self.flakelist:
            flake.update_flake()
def main():
    my_window = MyGame(SW, SH, "Snowfall")
    arcade.run()

if __name__ == "__main__":
    main()

