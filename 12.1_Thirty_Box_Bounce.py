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

        if self.x==0 and self.y==0:
            self.x+=1
            self.y+=1

        if self.x <= 30+self.w/2:
            self.dx *= -1
            self.c=(255,0,0)

        if self.x >= SW-30- self.w/2:
            self.dx *= -1
            self.c=(255,255,0)

        if self.y <= 30+self.w/2:
            self.dy *= -1
            self.c=(0,0,255)

        if self.y >= SH -30- self.w/2:
            self.dy *= -1
            self.c=(0,255,0)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

        self.box_list = []

        for i in range(box_num):
            w = random.randint(10,50)
            x = random.randint(30+w/2, )
            y = random.randint(100,500)
            dx = random.randint(-5,5)
            dy = random.randint(-5,5)
            c = (0,0,0)

            self.box = Box(x, y, w, dx, dy, c)


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