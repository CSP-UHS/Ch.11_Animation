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
box_num = 30


class Square():
    def __init__(self, x, y, dx, dy, w, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.w = w
        self.color = c
        if self.dx == 0:
            self.dx = random.randint(-20,20)
            print("zero")
        if self.dy == 0:
            self.dy = random.randint(-20,20)
            print("zero1")


    def drawsquare(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.w, self.w, self.color)


    def upatesquare(self):
        self.dy = self.dy - (9.81/60)
        self.x += self.dx
        self.y += self.dy

        if self.x <= ((self.w * 0.5) + 30):
            self.dx = (self.dx * -1)
            self.color = arcade.color.GAMBOGE

        if self.x >= (SW - (self.w * 0.5) - 30 ):
            self.dx = (self.dx * -1)
            self.color = arcade.color.HARLEQUIN

        if self.y <= ((self.w * 0.5) + 30):
            self.dy = (self.dy * -1) + (9.81/60)
            self.color = (arcade.color.BANANA_MANIA)

        if self.y >= (SH - (self.w * 0.5) - 30):
            self.dy = (self.dy * -1)
            self.color = (arcade.color.DARK_BYZANTIUM)


class MyGame(arcade.Window):
    def __init__(self, width, height, title, boxnum):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLACK)

        self.box_list = []
        for i in range(boxnum):
            self.square = Square(random.randint(80,520), random.randint(80,520), random.randint(-10,10), random.randint(-10,10), random.randint(5,50), arcade.color.KOBI)
            self.box_list.append(self.square)

    def on_draw(self):
        arcade.start_render()
        for box in self.box_list:
            box.drawsquare()

        arcade.draw_rectangle_filled(0,(0.5 * SH),60,SH,arcade.color.GAMBOGE)
        arcade.draw_rectangle_filled(SW, (0.5 * SH), 60, SH, arcade.color.HARLEQUIN)
        arcade.draw_rectangle_filled((SW*0.5),SH, SW, 60, arcade.color.DARK_BYZANTIUM)
        arcade.draw_rectangle_filled((SW*0.5),0, SW, 60, arcade.color.BANANA_MANIA)



    def on_update(self, dt):
        for box in self.box_list:
            box.upatesquare()


def main():
    mywindow = MyGame(SW,SH,"Title", box_num)
    arcade.run()


if __name__ == "__main__":
    main()
