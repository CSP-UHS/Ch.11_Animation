import arcade
import random

SW=640
SH=480

class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.dx=dx
        self.dy=dy
        self.rad=rad
        self.col=col


    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)

    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        # Bounce ball off edge of screen

        if self.pos_x < self.rad or self.pos_x > SW - self.rad:
            self.dx *= -1

        if self.pos_y < self.rad or self.pos_y > SH - self.rad:
            self.dy = self.dy * -1



class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.KOBE)
        self.ball_list=[]
        for i in range(100):
            r = random.randint(5,20)
            x=random.randint(r,SW-r)
            y=random.randint(r,SH-r)
            v1=random.randint(1,2)
            if v1==1:
                vx=random.randint(-5,-1)
            else:
                vx=random.randint(1,5)
            v2 = random.randint(1, 2)
            if v2 == 1:
                vy = random.randint(-5, -1)
            else:
                vy = random.randint(1, 5)
            c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            self.ball=Ball(x,y,vx,vy,r,c)
            self.ball_list.append(self.ball)

    def on_draw(self):
        arcade.start_render()
        for item in(self.ball_list):
            item.draw_ball()

    def on_update(self, dt):
        for item in (self.ball_list):
            item.update_ball()




def main():
    window=MyGame(SW,SH,"Wassup mf")
    arcade.run()


if __name__=="__main__":
    main()
