'''
30 BOX BOUNCE PROGRAM
--------------------
You will want to incorporate lists to modify the
Ball Bounce Program to create the following:

1.) Screen size 600 x 600
2.) Draw four 30px wide side rails on all four sides of the window
3.) Make each side rail a different color.
4.) Draw 30 black boxes(squares) of random size from 10-50 pixels
5.) Animate them starting at random speeds from -300 to +300 pixels/second. 
6.) All boxes must be moving.
7.) Start all boxes in random positions between the rails.
8.) Bounce boxes off of the side rails when the box edge hits the side rail.
9.) When the box bounces change its color to the rail it just hit.
10.)Title the window 30 Boxes

Helpful Hints:
1.) When you initialize the MyGame class create an empty list called self.boxlist=[] to hold all of your boxes.
2.) Then use a for i in range(30): list to instantiate boxes and append them to the list.
3.) In the on_draw section use: for box in self.boxlist: box.draw_box()
4.) Also in the on_draw section draw the side rails.
5.) In the on_update section use: for box in self.boxlist: box.update_box()
'''
import arcade
import random
SW = 600
SH = 600
WY = -1
WX = -1
BR = arcade.color.BLUE
TR = arcade.color.GREEN
LR = arcade.color.RED
RR = arcade.color.YELLOW
RW = 30
class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,size,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.col = col

    def draw_ball(self):
        arcade.draw_rectangle_filled(self.pos_x,self.pos_y,self.size,self.size,self.col)
    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        #bounce ball off of walls
        if self.pos_x > SW-self.size/2-RW:
            self.dx*=-1.1
            self.col = RR
        if self.pos_x < self.size/2+RW:
            self.dx*=-1.1
            self.col = LR
        if self.pos_y > SH - RW -self.size/2 :
            self.dy *= -1.1
            self.col = TR
        if self.pos_y < RW+self.size/2 :
            self.dy *= -1.1
            self.col = BR




class MyGame(arcade.Window):
    def __init__(self,width,height,title,):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.WHITE)
        self.balls =[]
        for i in range(30):
            r = random.randint(20,40)
            x = random.randint(r+RW,SW-RW-r)
            y = random.randint(r+RW,SW-RW-r)
            dx = random.randint(-3,-1) or random.randint(1,3)
            dy = random.randint(-3,-1) or random.randint(1,3)
            c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            ball = Ball(x,y,dx,dy,r,c)
            self.balls.append(ball)
    def on_draw(self):
        arcade.start_render()
        for ball in self.balls:
            ball.draw_ball()
            arcade.draw_rectangle_filled(300, 15, 540, RW, BR)
            arcade.draw_rectangle_filled(585, 300, RW, 540, RR)
            arcade.draw_rectangle_filled(300, 585, 540, RW, TR)
            arcade.draw_rectangle_filled(15, 300, RW, 540, LR)

    def on_update(self, dt):
        for ball in self.balls:
            ball.update_ball()










def myprogram():
    window = MyGame(SW,SH,"Drawing Example")


    arcade.run()

if __name__ == "__main__":
    myprogram()