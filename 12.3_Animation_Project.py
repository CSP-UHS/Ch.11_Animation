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

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)
        # arcade.draw_rectangle_filled(self.pos_x,self.pos_y,self.rad,self.rad,self.col,0)
    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy


        #bound ball off wall
        if self.pos_y < 0 - self.rad:
            self.pos_y = SH + self.rad
            self.pos_x = random.randint(0,SW)
        if self.pos_x < 0 - self.rad:
            self.pos_x += self.rad+2+SW
        if self.pos_x > SW + self.rad:
            self.pos_x -= self.rad+2+SW


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.DARK_ELECTRIC_BLUE)

        self.balls=[]
        for i in range(50):
            r = random.randint(1,5)
            x = random.randint(r,SW-r)
            y = random.randint(r,SH-r)
            dx = random.random()
            if dx > 0.5:
                dx *= -1
                dx += 0.3
            dy = random.randrange(15,30)
            dy *= -1
            col1 = arcade.color.BLUE


            #c=(random.randint(0,225),random.randint(0,255),random.randint(0,225))

            self.ball = Ball(x,y,dx,dy,r,col1)
            self.balls.append(self.ball)

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
