'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
SW = 600
SH = 600
WY = -1
WX = -1
class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col


    def draw_ball(self):
        arcade.draw_circle_outline(self.pos_x, self.pos_y, self.rad, arcade.color.BLACK, rad * 2.05)
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, arcade.color.WHITE)
        arcade.draw_circle_outline(self.pos_x, self.pos_y, self.rad / 1.5, self.col, rad)
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad / 1.6, self.col)
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad / 3, arcade.color.BLACK)
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad / 3.4, arcade.color.LIGHT_STEEL_BLUE)
        arcade.draw_arc_filled(self.pos_x, self.pos_y + self.rad / 1.15, rad * 1.2, rad * 1.25, arcade.color.BLACK, 0, 180, )
        arcade.draw_arc_filled(self.pos_x, self.pos_y + self.rad / 1.1, rad * 1.1, rad * 1.1, arcade.color.WHITE, 0, 180)
        arcade.draw_circle_filled(self.pos_x, self.pos_y + rad * 1.15, rad / 5, arcade.color.BLACK)
        arcade.draw_circle_filled(self.pos_x, self.pos_y + rad * 1.15, rad / 5.5, self.col)

    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        #bounce ball off of walls
        if self.pos_x > SW-self.rad*3 or self.pos_x < self.rad*3:
            self.dx*=-1

        if self.pos_y > SH - self.rad*3 or self.pos_y < self.rad*3:
            self.dy *= -1




class MyGame(arcade.Window):
    def __init__(self,width,height,title,):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.WHITE)
        self.balls =[]
        for i in range(10):
            r = random.randint(2,20)
            x = random.randint(r,SW-r)
            y = random.randint(r,SH-r)
            dx = random.randint(-3,3)
            dy = random.randint(-3,3)
            c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            ball = Ball(x,y,dx,dy,r,c)
            self.balls.append(ball)
    def on_draw(self):
        arcade.start_render()
        for ball in self.balls:
            ball.draw_ball(300,300)

    def on_update(self, dt):
        for ball in self.balls:
            ball.update_ball()



def myprogram():
    window = MyGame(SW,SH,"Drawing Example")
    arcade.run()

if __name__ == "__main__":
    myprogram()