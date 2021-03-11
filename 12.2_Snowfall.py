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
SW=640
SH=480

class Ball:
    def __init__(self,x,y,dx,dy,r,c):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.c=c

    def draw_ball(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.c)

    def update_ball(self):
        self.x+= self.dx
        self.y+= self.dy

        if self.x <= self.r or self.x >= SW - self.r:
            self.dx *= -1
        if self.y <= self.r or self.y >= SH - self.r:
            self.dy *= -1



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.ball = Ball(320,240,3,-2,15,arcade.color.ARMY_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.ball.draw_ball()

    def on_update(self, dt):
        self.ball.update_ball()

def main():
    window = MyGame(SW, SH, "Window")
    arcade.run()


if __name__ == "__main__":
    main()