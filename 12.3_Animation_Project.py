
import arcade
import random

SW = 600
SH = 600
FN = 300
BW = 15
hitlist = 0
for i in range(50):
    hitlist += 1

class Flake:
    def __init__(self, x, y, dy, r, c):
        self.x = x
        self.y = y
        self.dy = dy
        self.rad = r
        self.col = c

    def draw_flake(self):
        #little green men
        arcade.draw_rectangle_filled(self.x, self.y, self.rad, 5, self.col)
        #arcade.draw_triangle_filled(self.x, self.y, 20, 30, 40, 50, arcade.color.RED)
        arcade.draw_text("How is he not dead?!?!?!", self.x, self.y, arcade.color.WHITE, 11, 5)

    def update_flake(self):
        self.x += self.dy
        if self.x <= -self.rad:
            self.x = random.randint(SW, SW+100)
            self.y = random.randint(0, SW)
        if self.x > SW-self.rad or self.x < self.rad:
            self.dy *= -1
        if self.y > SH-self.rad or self.y < self.rad:
            self.dy *= -1

class MyGame(arcade.Window):
    def __init__(self, SW, SH, title):
        super().__init__(SW, SH, title)
        arcade.set_background_color(arcade.color.OCEAN_BOAT_BLUE)
        self.flakelist = []    #  hold all snow flake
        for i in range(FN):
            r = random.randint(10, 20)
            dy = random.randint(-4, -1)
            x = random.randint(0, SW)
            y = random.randint(0, SH)

            if i == 0:
                c = arcade.color.BROWN
            else:
                c = arcade.color.BROWN
            make_flake = Flake(x, y, dy, r, c)
            self.flakelist.append(make_flake)

    def on_draw(self):
        arcade.start_render()
        for flake in self.flakelist:
            flake.draw_flake()

        arcade.draw_rectangle_filled(SW, SH//2, 20, SH, arcade.color.GREEN)
        arcade.draw_rectangle_filled(BW//2, SH//2, BW, SH, arcade.color.GREEN)
        arcade.draw_rectangle_filled(SW//2, 3, SW, 25, arcade.color.GREEN)
        arcade.draw_rectangle_filled(SW//2, 600, SW, 25, arcade.color.GREEN)
        #character
        arcade.draw_triangle_filled(15, 15, 15, 15, 15, 15, arcade.color.DARK_GREEN)
        arcade.draw_rectangle_filled(40, 175, 80, 30, arcade.color.DARK_GREEN)
        # arcade.draw_rectangle_filled(40, 185, 10, 30, arcade.color.DARK_GREEN)
        # arcade.draw_rectangle_filled(40, 185, 10, 30, arcade.color.DARK_GREEN)
        arcade.draw_text("go the other way because I said so", 40, 175, arcade.color.WHITE, 5, 0)






    def on_update(self, dt):
        for flake in self.flakelist:
            flake.update_flake()
def main():
    my_window = MyGame(SW, SH, "The sailboat parade")
    arcade.run()

if __name__ == "__main__":
    main()

