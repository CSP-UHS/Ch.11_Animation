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
    def draw(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.width,self.width)

    def move(self):
        self.y_pos +=self.dy
        self.x_pos +=self.dx



def main():
    window = MyGame(SW, SH, "30 boxes")
    arcade.run()

if __name__=="__main__":
    main()