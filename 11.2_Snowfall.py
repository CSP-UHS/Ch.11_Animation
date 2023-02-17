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

SW=600
SH=600
Width=10

class Snow():
    def __init__(self,pos_x,pos_y,dy,rad,col,Width):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.dy=dy
        self.rad=rad
        self.col=col
        self.Width=Width


    def draw_Snow(self):
        arcade.draw_text("*",self.pos_x,self.pos_y,self.col)

    def update_Snow(self):
        self.pos_y+=self.dy
        # Snow reset
        if self.pos_y<0:
            self.pos_x=random.randint(0,600)
            self.pos_y=random.randint(600,700)


class outlines():
    def line(self):
        Width = 10
        arcade.draw_line(0, SH-Width/2, SW, SH-Width/2, arcade.color.WHITE, Width)
        arcade.draw_line(SW-Width/2, 0, SW-Width/2, SH, arcade.color.WHITE, Width)
        arcade.draw_line(Width/2, 0, Width/2, SH, arcade.color.WHITE, Width)
        arcade.draw_line(0, Width/2, SW, Width/2, arcade.color.WHITE, Width)



class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.KOBE)
        self.Snow_list=[]
        for i in range(300):
            r = random.randint(1,3)
            x=random.randint(r+Width,SW-r-Width)
            y=random.randint(r+Width,SH-r-Width)
            vy = random.randint(-4,-1)
            w=Width
            c=arcade.color.WHITE
            self.Snow=Snow(x,y,vy,r,c,w)
            self.Snow_list.append(self.Snow)


    def on_draw(self):
        arcade.start_render()
        outlines.line(self)
        for item in(self.Snow_list):
            item.draw_Snow()

    def on_update(self, dt):
        for item in (self.Snow_list):
            item.update_Snow()


def main():
    window=MyGame(SW,SH,"Snowfall")
    arcade.run()


if __name__=="__main__":
    main()