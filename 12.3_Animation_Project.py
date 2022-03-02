'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
SW=600
SH=600
import arcade
import random
class Box():
    def __init__(self,pos_x,pos_y,s,dx,dy,c):
        self.s=s
        self.dx=dx
        self.dy=dy
        self.c=c
        self.pos_x=pos_x
        self.pos_y=pos_y
    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x,self.pos_y,self.s,self.s,self.c)
    def update_box(self):
        self.s+=1
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        if self.s>SW/2:
            self.s-=1
        if self.pos_x==SW:
            self.pos_x=0
            self.pos_y=0
        arcade.set_background_color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

class MyGame(arcade.Window):
    def __init__(self,SW,SH,title):
        super().__init__(SW,SH,title)
        arcade.set_background_color(arcade.color.WHITE)
        self.box_list=[]
        for i in range(100):
            s=SH/12
            col=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            dx=50
            dy=50
            pos_x=random.randint(0,400)
            pos_y=pos_x
            box=Box(pos_x,pos_y,s,dx,dy,col)
            self.box_list.append(box)
    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.draw_box()
    def on_update(self,dt):
        for box in self.box_list:
            box.update_box()


def myprogram():
    window=MyGame(SW,SH,"Hermonator 3, Rise of the Machines")
    arcade.run()
if __name__=="__main__":
    myprogram()









