'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
import math
SW = 1440
SH = 780


class Car:
    def __init__(self, x, y, c, s):
        self.x = x
        self.y = y
        self.c = c
        self.s = s
        self.move = 0
        self.actual = 0

    def draw_car(self,x,y,radius):
        arcade.draw_circle_outline(x, y, radius * 1.1, arcade.color.BLACK, 6)
        arcade.draw_circle_filled(x, y, radius, arcade.color.WHITE)
        arcade.draw_circle_outline(x, y, radius * 1.1 / 1.5, arcade.color.BLACK, 8)
        arcade.draw_circle_filled(x, y, radius / 1.5, arcade.color.ORANGE)
        arcade.draw_circle_outline(x, y, radius * 1.2 / 3, arcade.color.BLACK, 8)
        arcade.draw_circle_filled(x, y, radius / 3, arcade.color.ASH_GREY)
        arcade.draw_rectangle_filled(x, y + radius * .9, radius * 1.65, 7, arcade.color.BLACK)
        arcade.draw_arc_outline(x, y + radius * .9, radius * 1.55, radius * 1.55, arcade.color.BLACK, 0, 180, 10)
        arcade.draw_arc_filled(x, y + radius * .9, radius * 1.5, radius * 1.5, arcade.color.WHITE, 0, 180)
        arcade.draw_circle_outline(x, y + radius * 1.25, radius / 4 * 1.2, arcade.color.BLACK, 5)
        arcade.draw_circle_filled(x, y + radius * 1.25, radius / 4, arcade.color.SKY_BLUE)

    def update_car(self):
        self.move += 1
        if self.move % 2 == 0:
            r = random.randint(0, 3)
            self.x += r
            self.y += r
            self.actual = r
        else:
            self.x -= self.actual
            self.y -= self.actual


class Tree:
    def __init__(self, h, x, s, r, t):
        self.h = h
        self.x = x
        self.s = s
        self.r = r
        self.t = t  # Type will be a random number, one or two, it will determine if it is a pine or normal tree

    def draw_tree(self):
        if self.t == 0:
            def leaf(x, h, rad, l):
                arcade.draw_circle_filled(rad * math.cos(math.radians(45 * l)) + x,
                                          rad * math.sin(math.radians(45 * l)) + h, rad, arcade.color.DARK_JUNGLE_GREEN)
            arcade.draw_rectangle_filled(self.x, self.h/2, self.r * 4 / 5, self.h, arcade.color.BROWN)
            arcade.draw_circle_filled(self.x, self.h, self.r * 1.75, arcade.color.BANGLADESH_GREEN)
            for i in range(8):
                leaf(self.x, self.h, self.r * 1.75, i)
        else:
            arcade.draw_rectangle_filled(self.x, self.h / 2, self.r * 4 / 5, self.h, arcade.color.BROWN)
            arcade.draw_polygon_outline(
                [[self.x, self.h * 1.4], [self.x + self.h * 3 / 10, self.h * 1.25 - self.h / 5],
                 [self.x + self.h * 3 / 10 - self.r / 2, self.h * 1.25 - self.h / 5],
                 [self.x + self.h * 3 / 9, self.h * 1.25 - 2 * self.h / 5],
                 [self.x + self.h * 3 / 9 - self.r / 2, self.h * 1.25 - 2 * self.h / 5],
                 [self.x + self.h * 3 / 8, self.h * 1.25 - 3 * self.h / 5],
                 [self.x + self.h * 3 / 8 - self.r / 2, self.h * 1.25 - 3 * self.h / 5],
                 [self.x + self.h * 3 / 7, self.h * 1.25 - 4 * self.h / 5],
                 [self.x + self.h * 3 / 7 - self.r / 2, self.h * 1.25 - 4 * self.h / 5],
                 [self.x + self.h * 3 / 6, self.h * 1.25 - self.h],
                 [self.x + self.h * 3 / 6 - self.r / 2, self.h * 1.25 - self.h],
                 [self.x + self.h * 3 / 6 + self.r / 2, self.h * 1.25 - self.h],
                 [self.x - self.h * 3 / 6, self.h * 1.25 - self.h],
                 [self.x - self.h * 3 / 7 + self.r / 2, self.h * 1.25 - 4 * self.h / 5],
                 [self.x - self.h * 3 / 7, self.h * 1.25 - 4 * self.h / 5],
                 [self.x - self.h * 3 / 8 + self.r / 2, self.h * 1.25 - 3 * self.h / 5],
                 [self.x - self.h * 3 / 8, self.h * 1.25 - 3 * self.h / 5],
                 [self.x - self.h * 3 / 9 + self.r / 2, self.h * 1.25 - 2 * self.h / 5],
                 [self.x - self.h * 3 / 9, self.h * 1.25 - 2 * self.h / 5],
                 [self.x - self.h * 3 / 10 + self.r / 2, self.h * 1.25 - self.h / 5],
                 [self.x - self.h * 3 / 10, self.h * 1.25 - self.h / 5]], arcade.color.BLACK, 3)
            arcade.draw_polygon_filled(
                [[self.x, self.h * 1.4], [self.x + self.h * 3 / 10, self.h * 1.25 - self.h / 5],
                 [self.x + self.h * 3 / 10 - self.r / 2, self.h * 1.25 - self.h / 5],
                 [self.x + self.h * 3 / 9, self.h * 1.25 - 2 * self.h / 5],
                 [self.x + self.h * 3 / 9 - self.r / 2, self.h * 1.25 - 2 * self.h / 5],
                 [self.x + self.h * 3 / 8, self.h * 1.25 - 3 * self.h / 5],
                 [self.x + self.h * 3 / 8 - self.r / 2, self.h * 1.25 - 3 * self.h / 5],
                 [self.x + self.h * 3 / 7, self.h * 1.25 - 4 * self.h / 5],
                 [self.x + self.h * 3 / 7 - self.r / 2, self.h * 1.25 - 4 * self.h / 5],
                 [self.x + self.h * 3 / 6, self.h * 1.25 - self.h],
                 [self.x + self.h * 3 / 6 - self.r / 2, self.h * 1.25 - self.h],
                 [self.x + self.h * 3 / 6 + self.r / 2, self.h * 1.25 - self.h],
                 [self.x - self.h * 3 / 6, self.h * 1.25 - self.h],
                 [self.x - self.h * 3 / 7 + self.r / 2, self.h * 1.25 - 4 * self.h / 5],
                 [self.x - self.h * 3 / 7, self.h * 1.25 - 4 * self.h / 5],
                 [self.x - self.h * 3 / 8 + self.r / 2, self.h * 1.25 - 3 * self.h / 5],
                 [self.x - self.h * 3 / 8, self.h * 1.25 - 3 * self.h / 5],
                 [self.x - self.h * 3 / 9 + self.r / 2, self.h * 1.25 - 2 * self.h / 5],
                 [self.x - self.h * 3 / 9, self.h * 1.25 - 2 * self.h / 5],
                 [self.x - self.h * 3 / 10 + self.r / 2, self.h * 1.25 - self.h / 5],
                 [self.x - self.h * 3 / 10, self.h * 1.25 - self.h / 5]], arcade.color.APPLE_GREEN)

    def update_tree(self):
        self.x += self.s

        if self.x > SW + 100:
            self.x -= SW + 100
            self.t = random.randint(0, 1)





class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)
        self.car = Car(1000, 120, arcade.color.ASH_GREY, 0)
        for x in range(-100, SW + 100, 25):
            height = 125
            base = 175
            diff = 25
            color = arcade.color.WHITE
            speed = 12.5
        self.trees = []
        for i in range(-100, SW + 100, 175):
            h = random.randint(400, 500)
            x = i
            s = 100
            r = random.randint(40, 60)
            t = random.randint(0, 1)
            tree = Tree(h, x, s, r, t)
            self.trees.append(tree)

    def on_draw(self):
        arcade.start_render()
        for tree in self.trees:
            tree.draw_tree()
        arcade.draw_lrtb_rectangle_filled(0, SW, 175, 0, arcade.color.AO)
        arcade.draw_lrtb_rectangle_filled(0, SW, 155, 25, arcade.color.GRAY)
        self.car.draw_car(1300,150,50)

    def on_update(self, dt):
        for tree in self.trees:
            tree.update_tree()
        self.car.update_car()
        print(dt)


def main():
    window = MyGame(SW, SH, "BB8")
    arcade.run()


if __name__ == "__main__":
    main()