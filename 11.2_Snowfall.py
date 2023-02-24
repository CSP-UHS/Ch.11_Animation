'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black backgrounddone
2.) Window title equals "Snowfall"done
3.) Crossbars 10 px wide. Snow must be outside!done
4.) Make snowflake radius random between 1-3done
5.) Randomly start snowflakes anywhere in the window. done
6.) Random downward speed of -4 to -1 done
7.) Start snowflakes again at random x from 0-600 and random y from 600-700 done
8.) Generate 300 snowflakes done
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white. done


'''
import arcade
import random
SW =600
SH=600

class Snowflake():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.dx=dx
        self.dy=dy
        self.rad=rad
        self.col=col
    def draw_snow(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)

    def update_snow(self):
        self.pos_y+=self.dy
        if self.pos_y<=0:
            self.pos_x= random.randint(0,600)
            self.pos_y=random.randint(600,700)


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowflake_list = []
        for i in range(300):
            r = random.randint(1, 3)
            x=random.randint(0,600)
            y=random.randint(0,600)
            vx=random.randint(-4,-1)
            vy=random.randint(-4,-1)
            c = arcade.color.WHITE
            # if vx==0:
            #     vx=random.randint(1,3)
            # if vy==0:
            #     vy=random.randint(-3,-1)
            if i == 0 :
                c = arcade.color.RED


            self.snowflake = Snowflake(x,y,vx,vy,r,c,)
            self.snowflake_list.append(self.snowflake)


    def on_draw(self):
        arcade.start_render()
        for item in(self.snowflake_list):
            item.draw_snow()
        arcade.draw_line(300,0,300,600,arcade.color.BROWN,10)
        arcade.draw_line(0, 300, 600, 300, arcade.color.BROWN, 10)
    def on_update(self, dt):
        for item in (self.snowflake_list):
            item.update_snow()
        # self.x +=2
        # self.y +=2

def main():
    window = MyGame(SW,SH,"Snowfall")
    arcade.run()

if __name__=="__main__":
    main()