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
class Box():
    def __init__(self,pos_x,pos_y,dx,dy,size,col):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.dx=dx
        self.dy=dy
        self.col=col
        self.size = size
    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x,self.pos_y,self.size,self.size,self.col)
    def update_box(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        if self.pos_x >= 570-self.size/2:
            self.col=arcade.color.YELLOW
            self.dx *= -1
        if self.pos_x <= 30+self.size/2:
            self.col=arcade.color.RED
            self.dx *= -1
        if self.pos_y>=570-self.size/2:
            self.col=arcade.color.GREEN
            self.dy *=-1
        if self.pos_y<=30+self.size/2:
            self.col=arcade.color.BLUE
            self.dy*=-1

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.WHITE)
        self.boxlist=[]
        for i in range(30):
            size = random.randint(10, 50)
            x=  random.randint(30+size,570-size)
            y=  random.randint(30+size,570-size)

            dx=random.randint(-6,6)
            dy=random.randint(-6,6)
            c=arcade.color.BLACK
            boxes=Box(x,y,dx,dy,size,c)
            self.boxlist.append(boxes)
    def on_draw(self):
        arcade.start_render()
        for ball in self.boxlist:
            ball.draw_box()
            arcade.draw_rectangle_filled(15, 300, 30, 540, arcade.color.RED)
            arcade.draw_rectangle_filled(300, 15, 540, 30, arcade.color.BLUE)
            arcade.draw_rectangle_filled(585, 300, 30, 540, arcade.color.YELLOW)
            arcade.draw_rectangle_filled(300, 585, 540, 30, arcade.color.GREEN)


    def on_update(self, dt):
        for ball in self.boxlist:
            ball.update_box()

def myprogram():
    window = MyGame(SW,SH,"Window")
    arcade.run()
if __name__=="__main__":
    myprogram()
