'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
SW = 600
SH = 600


class Cloud():
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_cloud(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)
        arcade.draw_circle_filled(self.pos_x+14, self.pos_y-6, self.rad, self.col)
        arcade.draw_circle_filled(self.pos_x-8, self.pos_y-3, self.rad, self.col)
        arcade.draw_circle_filled(self.pos_x+12, self.pos_y+2, self.rad, self.col)
        arcade.draw_circle_filled(self.pos_x+32, self.pos_y+2, self.rad, self.col)


    def update_cloud(self):
        self.pos_x += self.dx
        if self.pos_x == 630:
            self.pos_x = -40
        if self.dx == 0:
            self.dx += 1

class Car(Cloud):
    def __init__(self, pos_x, pos_y, dx, dy, hei, wid, col):
        super().__init__(pos_x, pos_y, dx, dy, hei, wid)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.wid = wid
        self.hei = hei
        self.col = col

    def draw_car(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.wid, self.hei, self.col)
        arcade.draw_rectangle_outline(self.pos_x, self.pos_y, self.wid, self.hei, arcade.color.BLACK)
        arcade.draw_circle_filled(self.pos_x+30, self.pos_y-14, 8, arcade.color.BLACK)
        arcade.draw_circle_filled(self.pos_x+30, self.pos_y-14, 5, arcade.color.COOL_GREY)
        arcade.draw_circle_filled(self.pos_x-30, self.pos_y-14, 8, arcade.color.BLACK)
        arcade.draw_circle_filled(self.pos_x-30, self.pos_y-14, 5, arcade.color.COOL_GREY)
        arcade.draw_rectangle_filled(self.pos_x-15, self.pos_y+18, self.wid-48, self.hei-3, self.col)
        arcade.draw_rectangle_outline(self.pos_x-15, self.pos_y+18, self.wid-48, self.hei-3, arcade.color.BLACK)
        arcade.draw_rectangle_outline(self.pos_x-22, self.pos_y+18, self.wid-68, self.hei-10, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.pos_x-22, self.pos_y+18, self.wid-68, self.hei-10, arcade.color.BLUE_YONDER)




    def update_car(self):
        self.pos_x += self.dx
        if self.pos_x < -50:
            self.pos_x = 650
            self.col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            self.dx = random.randint(-4, -2)




class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        self.clouds = []

        for i in range(20):
            rad = random.randint(10, 30)
            x = random.randint(-40, 620)
            y = random.randint(450, 600)
            dx = 0.5
            dy = 0
            c = arcade.color.WHITE

            cloud = Cloud(x, y, dx, dy, rad, c)

            self.clouds.append(cloud)

        self.cars = []

        for i in range(3):
            wid = 20
            hei = 80
            x = random.randint(620, 750)
            y = 220
            dx = random.randint(-4, -2)
            dy = 0
            c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            car = Car(x, y, dx, dy, wid, hei, c)

            self.cars.append(car)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(60, 550, 45, arcade.color.YELLOW)
        arcade.draw_circle_outline(60, 550, 45, arcade.color.BLACK)
        arcade.draw_rectangle_filled(250, 300, 100, 200, arcade.color.GRAY_BLUE)
        arcade.draw_rectangle_outline(250, 300, 100, 200, arcade.color.BLACK)
        arcade.draw_rectangle_filled(350, 270, 100, 140, arcade.color.SLATE_GRAY)
        arcade.draw_rectangle_outline(350, 270, 100, 140, arcade.color.BLACK)
        arcade.draw_rectangle_filled(450, 325, 100, 250, arcade.color.COOL_GREY)
        arcade.draw_rectangle_outline(450, 325, 100, 250, arcade.color.BLACK)
        arcade.draw_rectangle_filled(550, 300, 100, 200, arcade.color.CADET_GREY)
        arcade.draw_rectangle_outline(550, 300, 100, 200, arcade.color.BLACK)
        arcade.draw_rectangle_filled(50, 270, 100, 140, arcade.color.DAVY_GREY)
        arcade.draw_rectangle_outline(50, 270, 100, 140, arcade.color.BLACK)
        arcade.draw_rectangle_filled(150, 325, 100, 250, arcade.color.BATTLESHIP_GREY)
        arcade.draw_rectangle_outline(150, 325, 100, 250, arcade.color.BLACK)
        arcade.draw_rectangle_outline(300, 190, 600, 20, arcade.color.BLACK)
        arcade.draw_rectangle_filled(300, 190, 600, 20, arcade.color.LIGHT_GRAY)
        arcade.draw_rectangle_filled(300, 80, 600, 200, arcade.color.DIRT)
        arcade.draw_rectangle_filled(300, 155, 600, 50, arcade.color.BUD_GREEN)

        for cloud in self.clouds:
            cloud.draw_cloud()

        for car in self.cars:
            car.draw_car()



    def on_update(self, dt):
        for cloud in self.clouds:
            cloud.update_cloud()

        for car in self.cars:
            car.update_car()



def myprogram():
    window = MyGame(SW, SH, "Cityscape")

    arcade.run()

if __name__ == "__main__":
    myprogram()
