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
FN=300

class Flake:
    def __init__(self,x ,y ,dy,r,c):
        self.x=x
        self.y=y
        self.dy=dy
        self.r=r
        self.c=c

    def draw_flake(self):
        arcade.draw_circle_filled(self.x,self.y,self.r,self.c)

    def update_flake(self):
        self.y+= self.dy

        if self.y <= 0 - self.r:
            self.y=random.randint(SH, SH+100)
            self.x=random.randint(0,SW)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.flake_list=[]

        for i in range(FN):
            r = random.randint(1,3)
            dy = random.randint(-4,-1)
            x = random.randint(0,SW)
            y = random.randint(0, SH)

            if i==1:
                c = arcade.color.RED
            else:
                c = arcade.color.WHITE

            makeflake = Flake(x,y,dy,r,c)
            self.flake_list.append(makeflake)


    def on_draw(self):
        arcade.start_render()
        for flake in self.flake_list:
            flake.draw_flake()

        arcade.draw_rectangle_filled(SW//2,SH//2,10,SH,arcade.color.ALLOY_ORANGE)
        arcade.draw_rectangle_filled(SW // 2, SH // 2, SW, 10, arcade.color.ALLOY_ORANGE)

    def on_update(self, dt):
        for flake in self.flake_list:
            flake.update_flake()

def main():
    window = MyGame(SW, SH, "Snow Fall")
    arcade.run()

if __name__ == "__main__":
    main()