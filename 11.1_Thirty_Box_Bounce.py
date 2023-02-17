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

SW=600
SH=600
Width=30

class boxes():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col,Width):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.dx=dx
        self.dy=dy
        self.rad=rad
        self.col=col
        self.Width=Width


    def draw_boxes(self):
        arcade.draw_rectangle_filled(self.pos_x,self.pos_y,self.rad,self.rad,self.col)

    def update_boxes(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        # Bounce ball off edge of screen

        if self.pos_x < self.rad+self.Width/2:
            self.dx *= -1
            self.col=arcade.color.GREEN

        if self.pos_x > SW - self.rad-self.Width/2:
            self.dx *= -1
            self.col = arcade.color.YELLOW

        if self.pos_y < self.rad+self.Width/2:
            self.dy = self.dy * -1
            self.col = arcade.color.BLUE

        if self.pos_y > SH - self.rad-self.Width/2:
            self.dy = self.dy * -1
            self.col = arcade.color.RED


class outlines():
    def line(self):
        Width = 30
        arcade.draw_line(0, SH-Width/2, SW, SH-Width/2, arcade.color.RED, Width)
        arcade.draw_line(SW-Width/2, 0, SW-Width/2, SH, arcade.color.YELLOW, Width)
        arcade.draw_line(Width/2, 0, Width/2, SH, arcade.color.GREEN, Width)
        arcade.draw_line(0, Width/2, SW, Width/2, arcade.color.BLUE, Width)

    def corners(self):
        Width=30
        arcade.draw_rectangle_filled(Width/2,Width/2,Width,Width,arcade.color.WHITE)
        arcade.draw_rectangle_filled(SW-Width/2,Width/2,Width,Width,arcade.color.WHITE)
        arcade.draw_rectangle_filled(SW - Width / 2, SH-Width / 2, Width, Width, arcade.color.WHITE)
        arcade.draw_rectangle_filled(Width / 2, SH-Width / 2, Width, Width, arcade.color.WHITE)



class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.KOBE)
        self.boxes_list=[]
        for i in range(30):
            r = random.randint(10,50)
            x=random.randint(r+Width,SW-r-Width)
            y=random.randint(r+Width,SH-r-Width)
            v1=random.randint(1,2)
            if v1==1:
                vx=random.randint(-300,-1)
            else:
                vx=random.randint(1,300)
            v2 = random.randint(1, 2)
            if v2 == 1:
                vy = random.randint(-300,-1)
            else:
                vy = random.randint(1,300)
            rc=random.randint(1,4)
            if rc==1:
                c=arcade.color.RED
            elif rc==2:
                c=arcade.color.BLUE
            elif rc==3:
                c=arcade.color.GREEN
            else:
                c=arcade.color.YELLOW
            w=Width
            self.boxes=boxes(x,y,vx,vy,r,c,w)
            self.boxes_list.append(self.boxes)


    def on_draw(self):
        arcade.start_render()
        outlines.line(self)
        outlines.corners(self)
        for item in(self.boxes_list):
            item.draw_boxes()

    def on_update(self, dt):
        for item in (self.boxes_list):
            item.update_boxes()


def main():
    window=MyGame(SW,SH,"30 BOxes")
    arcade.run()


if __name__=="__main__":
    main()