'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
SW=750
SH=750


class FishBody():
    def __init__(self, posx, posy, dx, dy, rad, color):
        self.posx = posx
        self.posy = posy
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.color = color

    def draw_FishBody(self):
        arcade.draw_circle_filled(self.posx, self.posy, self.rad, self.color)

    def update_FishBody(self):
            self.posx+=self.dx
            self.posy+=self.dy
            if self.posy+self.rad == SH+30 and self.dy==1 and self.dx==1:
                self.dy=self.dy*-1
            if self.posy+self.rad == -30:
                self.dy = self.dy*-1
                self.dx = 0
            if self.posx == 1000 and self.dy == 0:
                self.dx = self.dx*-1
            if self.posx == -250 and self.dy == 0:
                self.dx = self.dx*-1


class FishEye():
    def __init__(self, posx, posy, dx, dy, rad, color):
        self.posx = posx
        self.posy = posy
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.color = color

    def draw_FishEye(self):
        arcade.draw_circle_filled(self.posx, self.posy, self.rad, self.color)

    def update_FishEye(self):
            self.posx+=self.dx
            self.posy+=self.dy
            if self.posy+(self.rad*5)==SH+30 and self.dy==1 and self.dx==1:
                self.dy=self.dy*-1
            if self.posy+self.rad == -30:
                self.dy = self.dy*-1
                self.dx = 0
            if self.posx == 1000 and self.dy == 0:
                self.dx = self.dx*-1
            if self.posx == -250 and self.dy == 0:
                self.dx = self.dx*-1

class Balls():
    def __init__(self,posx, posy, dx, dy, rad, color):
        self.posx = posx
        self.posy = posy
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.color = color


    def draw_balls(self):
        arcade.draw_circle_filled(self.posx, self.posy, self.rad, self.color)


    def update_balls(self):
        self.posx+=self.dx
        self.posy+=self.dy
        if self.posy == 750:
            self.posy = random.randint(-20, 1)
            self.posx = random.randint(0, 750)
            self.dy = random.randint(1, 5)

class Doors():
    def __init__(self, posx1, posy1, wid1, hgt1, col1, dx1, dy1):
        self.posx1 = posx1
        self.posy1 = posy1
        self.wid1 = wid1
        self.hgt1 = hgt1
        self.col1 = col1
        self.dx1 = dx1
        self.dy1 = dy1

    def draw_door(self):
        arcade.draw_rectangle_filled(self.posx1, self.posy1, self.wid1, self.hgt1, self.col1)

    def update_door(self):
        self.posx1 += self.dx1
        self.posy1 += self.dy1



class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLIZZARD_BLUE)
        self.ballsList = []

        for item in range(50):
            x = random.randint(1, SW-1)
            y = random.randint(1, 70)
            r = random.randint(3, 10)
            c = arcade.color.ALICE_BLUE
            dx = 0
            dy = random.randint(1, 5)

            ball = Balls(x, y, dx, dy, r, c)
            self.ballsList.append(ball)

        self.doorList = []

        for item in range(2):
            x1 = 250
            if item == 1:
                x1 = 500
            y1 = 375
            w1 = 500
            h1 = 750
            c1 = arcade.color.BROWN_NOSE
            dx1 = -4
            if item == 1:
                dx1 = 4
            dy1 = 0

            door = Doors(x1,y1,w1,h1,c1,dx1,dy1)
            self.doorList.append(door)

        self.fishbodyList = []

        for item in range(1):
            x2 = -5
            y2 = SH/2
            r = 50
            c = arcade.color.BLACK
            dx2 = 1
            dy2 = random.randint(-1, 1)
            if dy2 == 0:
                c = arcade.color.CYBER_YELLOW
                dx2 = 5
            if dy2 == 1:
                c = arcade.color.GUPPIE_GREEN
            if dy2 == -1:
                c = arcade.color.BOSTON_UNIVERSITY_RED

            fishbody = FishBody(x2, y2, dx2, dy2, r, c)
            fishfin = FishBody(x2-r, y2, dx2, dy2, r-25, c)
            self.fishbodyList.append(fishbody)
            self.fishbodyList.append(fishfin)

        self.fisheyeList = []

        for item in range(1):
            x = x2+15
            y = y2+15
            r = 10
            c = arcade.color.BLACK
            dx = dx2
            dy = dy2

            fisheye = FishEye(x, y, dx, dy, r, c)
            self.fisheyeList.append(fisheye)

    def on_draw(self):
        arcade.start_render()
        for ball in self.ballsList:
            ball.draw_balls()

        for fishbody in self.fishbodyList:
            fishbody.draw_FishBody()

        for fishfin in self.fishbodyList:
            fishfin.draw_FishBody()

        for fisheye in self.fisheyeList:
            fisheye.draw_FishEye()

        #backRocks
        arcade.draw_lrtb_rectangle_filled(0, 750, 60, 0, arcade.color.DIM_GRAY)

        #Outline
        arcade.draw_lrtb_rectangle_outline(0, 750, 750, 0, arcade.color.BLUE_GREEN, 25)

        #frontRocks
        rocklist = [(0, 50), (30, 70), (60, 40), (90, 30), (270, 70), (380, 50), (500, 40), (700, 75), (750, 30),
                    (750, 0), (0, 0)]
        arcade.draw_polygon_filled(rocklist, arcade.color.GRAY)

        for door in self.doorList:
            door.draw_door()


    def on_update(self, dt):
        for ball in self.ballsList:
            ball.update_balls()

        for fishbody in self.fishbodyList:
            fishbody.update_FishBody()

        for fishfin in self.fishbodyList:
            fishfin.draw_FishBody()

        for fisheye in self.fisheyeList:
            fisheye.update_FishEye()

        for door in self.doorList:
            door.update_door()

def myprogram():
    window = MyGame(SW, SH, "Fish")
    arcade.run()

if __name__ == "__main__":
    myprogram()
