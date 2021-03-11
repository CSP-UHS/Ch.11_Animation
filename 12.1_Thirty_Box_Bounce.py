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