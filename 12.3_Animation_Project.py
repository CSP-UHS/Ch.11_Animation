'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''


import arcade
import random

SH = 600
SW = 600

class Fire:
   def __init__(self, x, y, width, height, col):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.col = col
   def draw_fire(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.width,self.height,self.col)
   def update_fire(self):
        self.x = random.randint(200,400)
        self.y = 50
class OrangeFire:
   def __init__(self, x, y, width, height, col):
       self.x = x
       self.y = y
       self.width = width
       self.height = height
       self.col = col
   def draw_orangefire(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.width,self.height,self.col)
   def update_orangefire(self):
        self.x = random.randint(200,400)
        self.y = 50
class Fireflies:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
    def draw_flies(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_flies(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        if self.pos_y < 0:
            self.pos_y += random.randint(600, 700)
            self.dy = random.randint(-4, -1)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.balls = []
        for i in range(300):
            r = random.randint(1, 1)
            x = random.randint(0, SW)
            y = random.randint(600, 700)
            dx = 0
            dy = random.randint(-4, -1)
            c = arcade.color.WHITE
            flies = Fireflies(x, y, dx, dy, r, c)
            self.balls.append(flies)
        self.fires = []
        for i in range(30):
            x = random.randint(200,400)
            y = 50
            width = 40
            height = random.randint(20,500)
            col = arcade.color.RED
            fires = Fire(x,y,width,height,col)
            self.fires.append((fires))
        self.orangefires = []
        for i in range(30):
            x = random.randint(200, 400)
            y = 50
            width = 35
            height = random.randint(20, 450)
            col = arcade.color.ORANGE_RED
            orangefires = OrangeFire(x, y, width, height, col)
            self.orangefires.append((orangefires))
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(300,0,600,100,arcade.color.GRAY)
        arcade.draw_circle_filled(100,500,50,arcade.color.YELLOW)
        for flies in self.balls:
            flies.draw_flies()
        for fires in self.fires:
            fires.draw_fire()
        for orangefires in self.orangefires:
            orangefires.draw_orangefire()
        arcade.draw_rectangle_filled(300,0,250,50,arcade.color.DARK_BROWN)
    def on_update(self, dt):
        for flies in self.balls:
            flies.update_flies()
        for fires in self.fires:
            fires.update_fire()
        for orangefires in self.orangefires:
            orangefires.update_orangefire()


def main():
    window = MyGame(SW, SH, "Campfire")
    arcade.run()

if __name__ == "__main__":
    main()
