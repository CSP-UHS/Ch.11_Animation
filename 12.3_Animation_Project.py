'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
SW = 1440
SH = 780
class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx=dx
        self.dy=dy
        self.rad = rad
        self.col = col

    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

    def draw_ball(self):
        self.rad = (15/self.dy)

        # bound ball off wall
        if self.pos_y < 0 - self.rad:
            self.pos_y = SH + self.rad
            self.pos_x = random.randint(0, SW)
        if self.pos_x < 0 - self.rad:
            self.pos_x += self.rad + 2 + SW
        if self.pos_x > SW + self.rad:
            self.pos_x -= self.rad + 2 + SW

        if self.dy > -2:
            self.pos_y = SH - 100
            self.pos_x = random.randint(360, 1080)
            stop = False
            r = 0
            x2 = self.pos_x
            y2 = self.pos_y
            while not stop:
                r += 0.5
                x1 = x2
                y1 = y2
                x2 = random.randint(360,1080)
                y2 = random.randint(y1,680)
                arcade.draw_line(x1,y1,x2,y2,arcade.color.YELLOW,r)

                coinf = random.randint(0,3)
                for i in range(coinf):
                    x2 = random.randint(360, 1080)
                    y2 = random.randint(200, y1)
                    arcade.draw_line(x1, y1, x2, y2, arcade.color.YELLOW, r)

                if y2 == 200:
                    stop = True


            self.dy = (-1 * random.randint(6,20))
        else:
            # arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)
            arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.rad, self.rad, self.col, 0)
            self.dy = self.dy * 0.999






class Light():
    def __init__(self):
        self.pos_y = SH-100
        self.pos_x1 = random.randint(360,1080)
        self.rad2 = random.randint(1,200)
        self.pos_x2 = random.randint(360,1080)
        self.cou = 0

    def draw_light(self):
        arcade.draw_line(self.pos_x1,SH-100,self.pos_x2,250,arcade.color.YELLOW)

    def update_light(self):
        # self.cou += 1

        # if self.cou == 60:
        arcade.set_background_color(arcade.color.LIGHT_GRAY)
        self.pos_x1 = 2000
        self.pos_x2 = 2000
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)
        self.cou = 0




class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)

        self.balls=[]
        self.lits=[]
        for i in range(250):
            r = random.randint(1,5)
            x = random.randint(r,SW-r)
            y = random.randint(r,SH-r)
            dx = 0
            dx = random.random()
            if dx > 0.5:
                dx *= -1
                dx += 0.3
            dy = -1 * (random.random() * random.randint(1,10))
            col1 = arcade.color.BLUE


            #c=(random.randint(0,225),random.randint(0,255),random.randint(0,225))

            ball = Ball(x,y,dx,dy,r,col1)
            self.balls.append(ball)
        self.light = Light()
        self.lits.append(self.light)

    def on_draw(self):
        arcade.start_render()
        for ball in self.balls:
            ball.draw_ball()
        arcade.draw_rectangle_filled(SW/2,SH-100,SW/2,50,arcade.color.GRAY)
        arcade.draw_rectangle_filled(SW/2,SH-25,50,100,arcade.color.GRAY)
        arcade.draw_rectangle_filled(SW/2,200,SW/2,50,arcade.color.WOOD_BROWN)
        arcade.draw_rectangle_filled(385,100,30,200,arcade.color.WOOD_BROWN)
        arcade.draw_rectangle_filled(1055, 100, 30, 200, arcade.color.WOOD_BROWN)

    def on_update(self,dt):
        for ball in self.balls:
            ball.update_ball()

def myprogram():
    window = MyGame(SW,SH,"Anima Project")
    arcade.run()


if __name__ == "__main__":
    myprogram()
