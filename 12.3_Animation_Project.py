'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random

SW = 800
SH = 400


class Box:
    def __init__(self, x, y, dy, side, color):
        self.x = x
        self.y = y
        self.dy = dy
        self.side = side
        self.color = color
        self.rnum = 0
        self.rot = 0

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.side, self.side, self.color,self.rot)


    def update_box(self):
        self.dy = self.dy - (9.81 / 60)
        if self.y < 100:
            self.dy = 0
            self.y = 100
        self.y = self.y + self.dy


    def jump(self):
        # if guy in within certain range of "spike" jump
        self.dy = self.dy + 5
        self.y +=1
        self.rnum += 1

    def rotate(self):
        if self.rot <= self.rnum * 90:
            self.rot += 2
            if self.rot > self.rnum * 90:
                self.rot = self.rnum * 90



class Triangle:
    def __init__(self, x, y, dx, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.color = color

    def draw_triangle(self):
        arcade.draw_triangle_filled(self.x, self.y, self.x + 30, self.y, self.x +15, self.y + 30,self.color)

    def updatetri(self):
        self.x +=self.dx

        if self.x <= -10:
            self.x = random.randint(SW, SW + 20)


class Bruh(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.x = 200
        self.y = 100
        self.side = 30
        self.color = arcade.color.BLUE
        self.box = Box(200, 100, 0, 30, arcade.color.BLUE)

        self.trilist = []
        x = 300
        for i in range(4):
            x+= 150
            triangle = Triangle(x, 80, -2, arcade.color.RED)
            self.trilist.append(triangle)




    def on_draw(self):
        arcade.start_render()
        self.box.draw_box()

        for i in self.trilist:
            i.draw_triangle()

        arcade.draw_rectangle_filled(SW / 2, 35,  SW, 100, arcade.color.BLACK)

    def on_update(self, delta_time: float):

        self.box.update_box()
        self.box.rotate()

        for i in self.trilist:
            i.updatetri()
            if i.x - self.box.x >37 and i.x - self.box.x <40:
                self.box.jump()










def main():
    window = Bruh(SW, SH, "Bruh")
    arcade.run()


if __name__ == "__main__":
    main()