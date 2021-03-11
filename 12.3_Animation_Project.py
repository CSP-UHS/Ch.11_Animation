'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''

import arcade
import random
import time

SW = 600
SH = 600
snowflakes = 100


class Wind0s():
    def __init__(self, x, y, dx, dy, w, h, c, t, v,cond): #x,y velx, vely, width/radius,height,color, title, identifyer, ident 2
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.w = w
        self.h = h
        self.color = c
        self.t = t
        self.v = v
        self.window = cond

    def open(self):
        # print("woah")
        if self.window == False:
            self.window = True
        else:
            self.window = False


    #def push(self, cx, x, y):
    #    if abs(self.x - x) <= 40 and abs(self.y - y) <= 40:
    #        self.dx = self.dx + cx

    #def hold(self, x, y, dx, dy):
    #    if abs(self.x - x) <= 40 and abs(self.y - y) <= 40:
    #        self.x = self.x + dx
    #        self.y = self.y + dy
    #        self.y = self.y + self.dy

    def drawcircle(self):

        arcade.draw_rectangle_filled(300,595,600,15,arcade.color.BLUE)
        arcade.draw_text("Wind0s V.4.20.69", 25 , 585, arcade.color.WHITE, 12, 0, "center")
        arcade.draw_text(str(time.ctime()), 400, 585, arcade.color.WHITE, 12, 0, "center")

        if self.v == "na":
            arcade.draw_circle_filled(self.x, self.y, 15, self.color)
            arcade.draw_text(self.t, self.x -50, self.y - 30, arcade.color.WHITE, 12, 0, "center")

        if self.window == True:
            if self.v == "na": #if it has no identify do this
                arcade.draw_rectangle_filled(300,300,self.w,self.h,arcade.color.WHITE)
                arcade.draw_rectangle_filled(300,550,500,20,self.color)
                arcade.draw_text(self.t,80,540,arcade.color.WHITE_SMOKE,12)
                arcade.draw_rectangle_outline(300,305,self.w,self.h+10,arcade.color.COOL_GREY)

            if self.t =="Mozzerella Icecat": #mozz code lol
                off = 20
                arcade.draw_text("G",200+off,380,arcade.color.BLUE,30,0,"left")  #Draw Goongle logo
                arcade.draw_text("O0", 220+off, 380, arcade.color.DARK_GREEN, 30, 0, "left")
                arcade.draw_text("N", 260+off, 380, arcade.color.RED, 30, 0, "left")
                arcade.draw_text("G", 280+off, 380, arcade.color.GREEN, 30, 0, "left")
                arcade.draw_text("L", 300+off, 380, arcade.color.YELLOW, 30, 0, "left")
                arcade.draw_text("E", 320+off, 380, arcade.color.ORANGE, 30, 0, "left")

                arcade.draw_rectangle_outline(300,360,200,30,arcade.color.CADET_GREY) #Search Bar
                arcade.draw_rectangle_filled(400,360,30,30,arcade.color.BLUE)
                arcade.draw_circle_outline(404,364,7.5,arcade.color.COOL_GREY,3)
                arcade.draw_rectangle_filled(396,356,12,4,arcade.color.COOL_GREY,135)

            if self.t == "      Snowfall": #snowfall code
                #print(self.x)
                if self.v =="sf":
                    #print("bruh")
                    arcade.draw_circle_filled(self.x, self.y, self.w, arcade.color.RED)




    def updatecirlce(self):


        self.x += self.dx
        self.y += self.dy

        if self.v == "sf":
            self.dx = (self.dx + (random.randint(-1, 1)) * 0.1)
            if abs(self.dx) > 2:
                self.dx = self.dx * 0.5
            self.x += self.dx

            if self.y <= 50:
                self.y = 540
            if self.y >= 701:
                self.y = random.randint(-100, 0)
            if self.x > 545:
                self.x = 55
            if self.x < 55:
                self.x = 545


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        #Snowflakes Code
        flake_list = []
        for i in range(100):
            self.flake = Wind0s(random.randint(65, 525), random.randint(65, 525), 0, (-1 * random.randint(1, 4)), random.randint(1, 3),0, arcade.color.WHITE,"      Snowfall","sf",False)
            flake_list.append(self.flake)
            self.flake_list = flake_list
        #print(self.flake_list)

        self.window_list = [] #OVERALL WINDOWS LIST

        self.window = Wind0s(50, 40, 0, 0, 500, 500, arcade.color.PURPLE, "Mozzerella Icecat","na",False)
        self.window_list.append(self.window)
        self.window = Wind0s(50, 85, 0, 0, 500, 500, arcade.color.BLUE, "      Test Test","na",False)
        self.window_list.append(self.window)
        self.window = Wind0s(50, 130, 0, 0, 500, 500, arcade.color.BRICK_RED, "      Snowfall","na",False)
        self.window_list.append(self.window)
        self.window = Wind0s(50, 175, 0, 0, 500, 500, arcade.color.DARK_GREEN, "      Bounce","na",False)
        self.window_list.append(self.window)

    def on_draw(self):
        arcade.start_render()

        for box in self.window_list:
            box.drawcircle()

        for flake in self.flake_list:
            flake.drawcircle()





    def on_update(self, dt):

        for flake in self.flake_list:
            flake.updatecirlce()

        for box in self.window_list:
            box.updatecirlce()


    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print("Open")
        for flake in self.window_list:
            if abs(x - flake.x) <= 15 and abs(y - flake.y) <= 15:
                flake.open()

        for flake in self.flake_list:
            if abs(x - 50) <= 15 and abs(y - 130) <= 15:
                flake.open()


    # def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    #    for flake in self.window_list:
    #        flake.push(dy, x, y)

    #def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
    #    for flake in self.flake_list:
    #        flake.hold(x, y, dx, dy)


def main():
    mywindow = MyGame(SW, SH, "Snowfall")
    arcade.run()


if __name__ == "__main__":
    main()
