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

class Box():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x,self.pos_y,self.rad,self.rad,self.col)
    def update_box(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        #bounce ball off of walls
        if self.pos_x > SW - self.rad:
            self.dx *= -1
            self.col = arcade.color.YELLOW
        elif self.pos_x < self.rad:
            self.dx *= -1
            self.col = arcade.color.RED
        elif self.pos_y > SH - self.rad:
            self.dy *= -1
            self.col = arcade.color.GREEN
        elif self.pos_y < self.rad:
            self.dy *= -1
            self.col = arcade.color.BLUE

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.WHITE)
        self.boxes = []
        for i in range(30):
            r = random.randint(10,50)
            x = random.randint(30 + r, 570 - r)
            y = random.randint(30 + r, 570 - r)
            dx = random.randint(-5,5)
            dy = random.randint(-5,5)
            c = arcade.color.BLACK
            if dx == 0 and dy == 0:
                dx = 1
                dy = 1
            if dx == 0:
                dx = 1
            if dy == 0:
                dy = 1
            self.box = Box(x,y,dx,dy,r,c)
            self.boxes.append(self.box)
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(SW / 2, 15, SW - 60, 30, arcade.color.BLUE)
        arcade.draw_rectangle_filled(SW / 2, SH - 15, SH - 60, 30, arcade.color.GREEN)
        arcade.draw_rectangle_filled(15, SH / 2, 30, SH - 60, arcade.color.RED)
        arcade.draw_rectangle_filled(SW - 15, SH / 2, 30, SH - 60, arcade.color.YELLOW)
        for box in self.boxes:
            box.draw_box()
    def on_update(self, dt):
        for box in self.boxes:
            box.update_box()

def myprogram():
    window = MyGame(SW,SH,"30_Boxes")
    arcade.run()

if __name__ == "__main__":
    myprogram()