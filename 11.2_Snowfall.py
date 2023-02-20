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
SW = 600
SH = 600


class Snowflake():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
    def draw_snow(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y ,self.rad,self.col)

    def draw_window(self):
        arcade.draw_rectangle_filled(300,300,600,10,arcade.color.REDWOOD)
        arcade.draw_rectangle_filled(300,300,600,10,arcade.color.REDWOOD,90)

    def update_snow(self):
        self.pos_y+=self.dy
        if self.pos_y<=0:
             self.pos_y = random.randint(600,700)
             self.pos_x = random.randint(0, 600)


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowflakes_list=[]
        for i in range(300):
            r=random.randint(1,3)
            x=random.randint(1,600)
            y=random.randint(0,600)
            vx=random.randint(-4,-1)
            vy=random.randint(-4,-1)
            c = arcade.color.WHITE
            w = arcade.color.RED
            self.snowflake = Snowflake(x,y,vx,vy,r,c)
            self.snowflakes_list.append(self.snowflake)
        self.redflake = Snowflake(x, y, vx, vy, 3, w)
        self.snowflakes_list.append(self.redflake)

    def on_draw(self):
        arcade.start_render()
        for item in (self.snowflakes_list):
            item.draw_snow()
        arcade.draw_rectangle_filled(300, 300, 600, 10, arcade.color.REDWOOD)
        arcade.draw_rectangle_filled(300, 300, 600, 10, arcade.color.REDWOOD, 90)


    def on_update(self,dt):
        for item in (self.snowflakes_list):
            item.update_snow()

def main():
    window = MyGame(SW,SH,"Snowfall")
    arcade.run()
if __name__ == "__main__":
    main()