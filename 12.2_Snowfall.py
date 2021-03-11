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
box_num=30

# arcade.draw_rectangle_filled(15, 300, 30, 540, (255, 0, 0))
# arcade.draw_rectangle_filled(300, 15, 540, 30, (0, 0, 255))
# arcade.draw_rectangle_filled(300, 585, 540, 30, (0, 255, 0))
# arcade.draw_rectangle_filled(585, 300, 30, 540, (255, 255, 0))

class Box:
    def __init__(self,x,y,dx,dy,w,c):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.w=w
        self.c=c

    def draw_box(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.w,self.w,self.c)

    def update_box(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.w+30 or self.x >= SW -30- self.w:
            self.dx *= -1
        if self.y <= self.w+30 or self.y >= SH -30- self.w:
            self.dy *= -1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.boxlist=[]
        arcade.set_background_color(arcade.color.WHITE)
        self.box=Box(random.randint(100,500),random.randint(100,500),random.randint(-5,5),random.randint(-5,5),
random.randint(10, 50), (0,0,0))

    def on_draw(self):
        arcade.start_render()
        self.box.draw_box()

    def on_update(self, dt):
        self.box.update_box()

def main():
    window = MyGame(SW, SH, "Thirty Boxes")
    arcade.run()

if __name__=="__main__":
    main()