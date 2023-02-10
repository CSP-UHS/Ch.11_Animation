import arcade
import random
SW = 640
SH = 480


class Ball():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y ,self.rad,self.col)

    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy

    #bounce ball off edge of screens

        if self.pos_x <self.rad or self.pos_x > SW - self.rad:
            self.dx*=-1
        if self.pos_y < self.rad or self.pos_y > SH - self.rad:
            self.dy *= -1


class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.ball_list=[]
        for i in range(100):
            r=random.randint(10,30)
            x=random.randint(r,SW-r)
            y=random.randint(r,SH-r)
            vx=random.randint(-3,3)
            vy=random.randint(-3,3)
            c=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
            if vx ==0:
                vx = random.randint(1,3)
            if vy ==0:
                vy = random.randint(-3,-1)
            self.ball = Ball(x,y,vx,vy,r,c)
            self.ball_list.append(self.ball)


    def on_draw(self):
        arcade.start_render()
        for item in (self.ball_list):
            item.draw_ball()

    def on_update(self,dt):
        for item in (self.ball_list):
            item.update_ball()

def main():
    window = MyGame(SW,SH,"Drawing Example")
    arcade.run()
if __name__ == "__main__":
    main()