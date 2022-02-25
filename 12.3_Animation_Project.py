'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random

SW = 600
SH = 600

class Snow():
    def __init__(self, pos_x, pos_y, dx, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.rad = rad
        self.col = col

    def draw_snowflake(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)

    def update_snowflake(self):
        self.pos_x += self.dx

        # respawn snowflake right of screen
        if self.pos_x < self.rad:
            self.pos_x = random.randint(600,700)

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.WHITE)
        self.snowflakes = []
        for i in range(1200):
            r = random.randint(3,7)
            x = random.randint(0,600)
            y = random.randint(0,600)
            dx = random.randint(-8,-4)
            c = arcade.color.WHITE
            self.snowflake = Snow(x,y,dx,r,c)
            self.snowflakes.append(self.snowflake)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(SW/2,SH/2,SW/2,arcade.color.BABY_BLUE_EYES)
        arcade.draw_arc_filled(SW/2,SH/6,SW,SH/2,arcade.color.WHITE,0,180,180)
        for snowflake in self.snowflakes:
            snowflake.draw_snowflake()
        arcade.draw_rectangle_filled(SW/2,SH/2,5,SH,arcade.color.RED)
        arcade.draw_rectangle_filled(SW/2,SH/2,SW,5,arcade.color.RED)
        arcade.draw_circle_outline(SW/2,SH/2,SW/10,arcade.color.RED,5)
    def on_update(self, dt):
        for snowflake in self.snowflakes:
            snowflake.update_snowflake()

def myprogram():
    window = MyGame(SW,SH,"Sniper in a Storm")
    arcade.run()

if __name__ == "__main__":
    myprogram()