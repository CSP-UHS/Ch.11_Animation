import arcade
import random
SW=640
SH=480

class Ball:
    def __init__(self,pos_x,pos_y,dx,dy,rad,color):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.dx=dx
        self.dy=dy
        self.rad=rad
        self.color=color

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.color)

    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
    # Bouncing the ball off the edges
        if self.pos_x<self.rad or self.pos_x>SW-self.rad:
            self.dx*=-1
        if self.pos_y<self.rad or self.pos_y>SH-self.rad:
            self.dy*=-1

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)
        self.ball_list=[]
        for i in range(10):
            self.dx = random.randint(-2, 2)
            self.dy = random.randint(-2, 2)
            self.color= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.ball=Ball(SW/2,SW/2,self.dx,self.dy,15,self.color)
            self.ball_list.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        for ball in self.ball_list:
            ball.draw_ball()

    def on_update(self, dt):
        for ball in self.ball_list:
            ball.update_ball()

def main():
    window=MyGame(SW,SH,"Animation")
    arcade.run()

if __name__=="__main__":
    main()