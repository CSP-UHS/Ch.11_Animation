

'''
'''

import arcade
import random
import time

SW = 1300
SH = 800
snowflakes = 30


#keyboard stuffs
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",",","'",":","0","1","2","3","4","5","6","7","8","9"]
numbers = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,46,44,39,59,48,49,50,51,52,53,54,55,56,57]
line_list = [0]


class Wind0s():
    def __init__(self, x, y, dx, dy, w, h, c, t, v, cond):  # x,y vel x, vel y, width/radius, height, color, title, identifier, ident 2
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
        self.prog = 0
        self.curx = 300
        self.cury = 300
        self.note = ""
        self.line = 0
        self.timer = 0
        self.curscolor = arcade.color.BLACK

    def open(self):  # called to open window
        # print("woah")
        if self.window == False:
            self.window = True
        else:
            self.window = False
            self.prog = 0  # reset animation

    # def push(self, cx, x, y):
    #    if abs(self.x - x) <= 40 and abs(self.y - y) <= 40:
    #        self.dx = self.dx + cx

    def hold(self, x, y, dx, dy): # Moves the windows and any objects in the windows "home point" with the mouse drag.
        # if abs(self.x - x) <= 40 and abs(self.y - y) <= 40:
        self.curx = self.curx + dx
        self.cury = self.cury + dy

    def notes(self,key,mod):
        if self.t == "        Notes":
            pos = 0
            print(key)
            if key == 32:
                print("space")
                self.note = self.note + " "
            if key == 65288:
                print("back")
                self.note = self.note[:-1]
            if key == 65293:
                print("return")
                self.note = self.note + "\n"
            if key == 65289:
                self.note = self.note + "    "





            pos = -1
            for i in numbers:
                pos = pos + 1
                if i == key:
                    #print("test")
                    key = letters[pos]
                    if mod == 1:
                        self.note = self.note + key.upper()
                    else:
                        self.note = self.note + key




    # This does wayyyy more than draw circles but im to lazy to rename it. Responsible for drawing everything on screen. CAUTION, Held together with magic and tape so yeah.
    def drawcircle(self):

        arcade.draw_rectangle_filled((0.5 * SW), (SH - 5), SW, 15, arcade.color.BLUE)  # Header
        arcade.draw_text("Wimd0s V.4.20.69", 25, (SH - 15), arcade.color.WHITE, 12, 0, "center")
        arcade.draw_text(str(time.ctime()), (SW - 190), (SH - 15), arcade.color.WHITE, 12, 0, "center")

        if self.v == "na": #Icons on desktop
            arcade.draw_circle_filled(self.x, self.y, 15, self.color)
            arcade.draw_text(self.t, self.x - 50, self.y - 30, arcade.color.WHITE, 12, 0, "center")

        if self.window == True:
            if self.v == "na":  # if window has no identity do this (draws blank window)
                # print("test")
                if self.prog <= 500: # opening animation
                    arcade.draw_rectangle_outline(self.curx, self.cury, self.prog, self.prog, arcade.color.COOL_GREY)
                if self.prog >= 500: # Blank window
                    arcade.draw_rectangle_filled(self.curx, self.cury, self.w, self.h, arcade.color.WHITE)
                    arcade.draw_rectangle_filled(self.curx, self.cury + 250, 500, 20, self.color)
                    arcade.draw_text(self.t, self.curx - 230, self.cury + 240, arcade.color.WHITE_SMOKE, 12)
                    arcade.draw_rectangle_outline(self.curx, self.cury + 5, self.w, self.h + 10, arcade.color.COOL_GREY)


            if self.prog >= 500:
                if self.t == "Mozzerella Icecat":  # mozz code

                    # Draw Goongle logo
                    off = 20
                    arcade.draw_text("G", self.curx - 100 + off, self.cury + 80, arcade.color.BLUE, 30, 0, "left")
                    arcade.draw_text("O0", self.curx - 80 + off, self.cury + 80, arcade.color.DARK_GREEN, 30, 0, "left")
                    arcade.draw_text("N", self.curx - 40 + off, self.cury + 80, arcade.color.RED, 30, 0, "left")
                    arcade.draw_text("G", self.curx - 20 + off, self.cury + 80, arcade.color.GREEN, 30, 0, "left")
                    arcade.draw_text("L", self.curx + off, self.cury + 80, arcade.color.YELLOW, 30, 0, "left")
                    arcade.draw_text("E", self.curx + 20 + off, self.cury + 80, arcade.color.ORANGE, 30, 0, "left")

                    arcade.draw_rectangle_outline(self.curx, self.cury + 60, 200, 30,
                                                  arcade.color.CADET_GREY)  # Search Bar
                    arcade.draw_rectangle_filled(self.curx + 100, self.cury + 60, 30, 30, arcade.color.BLUE)
                    arcade.draw_circle_outline(self.curx + 104, self.cury + 64, 7.5, arcade.color.COOL_GREY, 3)
                    arcade.draw_rectangle_filled(self.curx + 96, self.cury + 65, 12, 4, arcade.color.COOL_GREY, 135)

                if self.t == "      Snowfall":  # snowfall code
                    # print(self.v)
                    if self.v == "sf":
                        # print("bruh")
                        arcade.draw_circle_filled(self.x + (self.curx - 300), self.y + (self.cury - 300), self.w,
                                                  arcade.color.BLACK)

                if self.t == "      Bounce":  # Bounce code
                    # print(self.v)
                    if self.v == "ball":
                        # print(self.v)
                        arcade.draw_circle_filled((self.x + (self.curx - 300)), (self.y + (self.cury - 300)), self.w,
                                                  self.color)  # draws ball

                if self.t == "        Notes":


                    if self.curscolor == arcade.color.WHITE:
                        arcade.draw_text(self.note, self.curx - 240, self.cury + 240, arcade.color.BLACK,
                                         anchor_y="top")
                    else:
                        arcade.draw_text(self.note + "|", self.curx - 240, self.cury + 240, self.curscolor,
                                         anchor_y="top")
                    arcade.draw_text(self.note,self.curx - 240, self.cury + 240, arcade.color.BLACK ,anchor_y="top")



    def updatecirlce(self):
        if self.timer >= 60:
            self.timer = 0
        else:
            self.timer += 1

        if self.timer == 30:
            self.curscolor = arcade.color.WHITE
        if self.timer == 0:
            self.curscolor = arcade.color.BLACK

        if self.v == "sf" and self.v != "ball":  # movement for snowflakes
            self.y = self.y + self.dy  # + (0 * (self.cury - 300))
            self.dx = (self.dx + (random.randint(-1, 1)) * 0.1)
            if abs(self.dx) > 2:
                self.dx = self.dx * 0.5
            self.x += (self.dx)  # + (0* (self.curx - 300))
            # print(self.curx)

            if self.y <= (50):  # + (self.cury - 300)):
                self.y = (540)
            if self.y >= (701):  # + (self.cury - 300)):
                self.y = (random.randint(-100, 0))  # + (self.cury - 300))
            if self.x > (545):  # + (self.curx - 300)):
                self.x = (55)
            if self.x < (55):  # + (self.curx - 300)):
                self.x = (545)

        if self.v == "ball" and self.v != "sf":  # movement for balls
            self.dx = self.dx
            self.dy = self.dy - (9.81 / 60)
            self.x += self.dx
            self.y += self.dy

            if self.x <= 65 or self.x >= 535:
                self.dx = (self.dx * -1)
                # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if self.y >= 535 or self.y <= 75:
                self.dy = (self.dy * -1) + (9.81 / 60)
                # self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if self.y <= 5:
                self.y = 16

        if self.window == True:  # window open animation
            self.prog = self.prog + 50


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title,antialiasing=False)
        arcade.set_background_color(arcade.color.BLACK)

        self.note = ""

        # Snowflakes Code
        flake_list = []
        for i in range(snowflakes):
            self.flake = Wind0s(random.randint(65, 525), random.randint(65, 525), 0, (-1 * random.randint(1, 4)),
                                random.randint(1, 3), 0, arcade.color.WHITE, "      Snowfall", "sf", False)
            flake_list.append(self.flake)
            self.flake_list = flake_list
        # print(self.flake_list)

        # OVERALL WINDOWS LIST (Makes "Shortcut" and defines some parameters of the window once its open)
        self.window_list = []

        self.window = Wind0s(50, 40, 0, 0, 500, 500, arcade.color.PURPLE, "Mozzerella Icecat", "na", False)
        self.window_list.append(self.window)
        self.window = Wind0s(50, 85, 0, 0, 500, 500, arcade.color.BLUE, "        Notes", "na", False)
        self.window_list.append(self.window)
        self.window = Wind0s(50, 130, 0, 0, 500, 500, arcade.color.BRICK_RED, "      Snowfall", "na", False)
        self.window_list.append(self.window)
        self.window = Wind0s(50, 175, 0, 0, 500, 500, arcade.color.DARK_GREEN, "      Bounce", "na", False)
        self.window_list.append(self.window)
        # self.window = Wind0s(50, 220, 0, 0, 500, 500, arcade.color.BANANA_MANIA, "      Hermon", "na", False)
        # self.window_list.append(self.window)

        # Bounce This if for the actual balls in the window, defines starting x and y as well as velocitys, radius and colors
        ball_list = []
        self.ball = Wind0s(280, 500, 3, 0, 15, 0, arcade.color.BLUE, "      Bounce", "ball", False)
        ball_list.append(self.ball)
        self.ball = Wind0s(320, 500, -3, 0, 15, 0, arcade.color.BLUE, "      Bounce", "ball", False)
        ball_list.append(self.ball)
        self.ball_list = ball_list
        #print(ball_list)

    def on_draw(self):
        arcade.start_render()

        for box in self.window_list:
            box.drawcircle()

        for flake in self.flake_list:
            if flake.window == True:
                flake.drawcircle()

        for ball in self.ball_list:
            if ball.window == True:
                ball.drawcircle()

    def on_update(self, dt):

        for box in self.window_list:
            if box.window == True:
                box.updatecirlce()

        for flake in self.flake_list:
            if flake.window == True:
                flake.updatecirlce()

        for ball in self.ball_list:
            if ball.window == True:
                # print("balls")
                ball.updatecirlce()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # print("Open")
        for flake in self.window_list:
            if abs(x - flake.x) <= 15 and abs(y - flake.y) <= 15:
                flake.open()

        for flake in self.flake_list:
            if abs(x - 50) <= 15 and abs(y - 130) <= 15:
                flake.open()

        for flake in self.ball_list:
            if abs(x - 50) <= 15 and abs(y - 175) <= 15:
                # print("hrrng")
                flake.open()

    # def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
    #    for flake in self.window_list:
    #        flake.push(dy, x, y)

    # So there is a lot going on here, this sends paramiters to the "hold" function in the WinD0s class. It looks for where the mouse is and sends that and the mouses movememt to hte hold function.
    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, buttons: int, modifiers: int):
        # print("test")
        for box in self.window_list:  # For dragging windows around
            if box.window == True:
                if y - box.cury >= 235 and y - box.cury <= 265:
                    if x - box.curx >= -250 and x - box.curx <= 250:
                        # print("test pass")
                        box.hold(x, y, dx, dy)

        for ball in self.ball_list:  # for the movement of the balls in the window while dragging
            if ball.window == True:
                if y - ball.cury >= 235 and y - ball.cury <= 265:
                    if x - ball.curx >= -250 and x - ball.curx <= 250:
                        # print("test pass")
                        ball.hold(x, y, dx, dy)

        for flake in self.flake_list: # for the movement of the snowflakes in the window while dragging
            if flake.window == True:
                if y - flake.cury >= 235 and y - flake.cury <= 265:
                    if x - flake.curx >= -250 and x - flake.curx <= 250:
                        # print("test pass")
                        flake.hold(x, y, dx, dy)

    def on_key_press(self, symbol: int, modifiers: int):
        for box in self.window_list:
            if box.t == "        Notes":
                if box.window == True:
                    self.note = symbol
                    box.notes(self.note,modifiers)











def main():
    mywindow = MyGame(SW, SH, "Wimd0s")
    arcade.run()


if __name__ == "__main__":
    main()
