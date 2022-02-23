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

#CHANGE TO BOX CODE FROM BALL CODE

import arcade
import random
SW = 600
SH = 600

class Ball():
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        #bounce ball off of walls
        if self.pos_x > SW-self.rad or self.pos_x < self.rad:
            self.dx *= -3
        if self.pos_y > SH - self.rad or self.pos_y < self.rad:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ARYLIDE_YELLOW)
        self.balls = []
        for i in range(275):
            r = random.randint(2, 20)
            x = random.randint(r, SW-r)
            y = random.randint(r, SH - r)
            dx = random.randint(-3, 3)
            dy = random.randint(-3, 3)
            c = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

            ball = Ball(x, y, dx, dy, r, c)
            self.balls.append(ball)
    def on_draw(self):
        arcade.start_render()
        for ball in self.balls:
            ball.draw_ball()

    def on_update(self, dt):
        for ball in self.balls:
            ball.update_ball()



def myprogram():
    window = MyGame(SW, SH, "Test")
    arcade.run()

if __name__ == "__main__":
    myprogram()
