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
width=20
col=(255,0,0)

class Box:
    def __init__(self):
        self.x=random.randint(30+self.width, SW-30-self.width)
        self.y=random.randint(30+self.width, SH-30-self.width)
        self.width=width
        self.dx=random.randint(-300,300)
        self.dy=random.randint(-300,300)
        self.color=col


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        self.width=SW
        self.height=SH
        self.title="30 boxes"


def main():
    window = MyGame(SW, SH, "30 boxes")
    arcade.run()

if __name__=="__main__":
    main()