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


c1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Right Wall
c2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Left Wall
c3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Top Wall
c4 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Bottom Wall


class Square():

    def __init__(self,pos_x,pos_y,dx,dy,w,h,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.w = w
        self.h = h
        self.col = col
    def draw_barrier(self):
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        arcade.draw_rectangle_filled(585, 300, 30, 540,c)
        arcade.draw_rectangle_filled(15, 300, 30, 540, (255, 255, 255))
        arcade.draw_rectangle_filled(300, 585, 30, 540, (255, 255, 255),90)
        arcade.draw_rectangle_filled(300, 15, 30, 540, (255, 255, 255),90)
    def draw_square(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y ,self.w,self.h,self.col)

    def update_square(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
    # D = derivative or velocity in direction
    #bounce ball off edge of screens

        if self.pos_x <(self.h/2)+30: #left wall
            self.dx*=-1
            self.col = c2
        elif self.pos_x > SW - (self.h/2)-30: #Right Wall
            self.dx*=-1
            self.col = c1
        elif self.pos_y < (self.h/2)+30: #Bottom wall
            self.dy*=-1
            self.col = c4

        elif self.pos_y > SH - (self.h/2)-30: #Top Wall
            self.dy *= -1
            self.col = c3



class MyGame(arcade.Window):

    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        arcade.set_background_color(c)
        # self.c1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Right Wall
        # self.c2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Left Wall
        # self.c3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Top Wall
        # self.c4 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) #Bottom Wall

        self.box_list=[]
        for i in range(30):
            l=random.randint(10,50)
            x=random.randint(l+30,(SW-l)-30)
            y=random.randint(l+30,(SH-l)-30)
            vx=random.randint(-5,5)
            vy=random.randint(-5,5)
            c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if vx ==0:
                vx = random.randint(1,3)
            if vy ==0:
                vy = random.randint(-3,-1)
            self.square = Square(x,y,vx,vy,l,l,c)
            self.box_list.append(self.square)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(585, 300, 30, 540, c1)
        arcade.draw_rectangle_filled(15, 300, 30, 540, c2)
        arcade.draw_rectangle_filled(300, 585, 30, 540, c3, 90)
        arcade.draw_rectangle_filled(300, 15, 30, 540, c4, 90)

        for item in (self.box_list):
            item.draw_square()

        # c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # arcade.draw_rectangle_filled(585, 300, 30, 540, (0,255,255))
        # arcade.draw_rectangle_filled(15, 300, 30, 540, (255, 0, 255))
        # arcade.draw_rectangle_filled(300, 585, 30, 540, (255, 255, 0), 90)
        # arcade.draw_rectangle_filled(300, 15, 30, 540, (0, 0, 255), 90)
    def on_update(self,dt):
        for item in (self.box_list):
            item.update_square()


def main():
    window = MyGame(SW,SH,"30 Squares - Oded")
    arcade.run()


if __name__ == "__main__":
    main()
