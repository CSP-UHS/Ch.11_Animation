import arcade
import random
SW =500
SH=500
player_x = random.randint(350,400)
player_y = random.randint(250,300)

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
        arcade.draw_circle_outline(self.pos_x,self.pos_y,self.rad,arcade.color.BLACK,3)
        arcade.draw_circle_filled(self.pos_x-15,self.pos_y,10,arcade.color.BLACK,4)
        arcade.draw_circle_filled(self.pos_x,self.pos_y+15,10,arcade.color.BLACK,7)
        arcade.draw_circle_filled(self.pos_x+7,self.pos_y-10,10,arcade.color.BLACK)


    def update_ball(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy

        #bounce ball off edge of screen
        if self.pos_x < self.rad or self.pos_x > SW-self.rad:
            self.dx*=-1
        if self.pos_y < self.rad or self.pos_y > SH-self.rad:
            self.dy*=-1

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.GREEN)
        self.ball_list = []
        for i in range(1):
            r = 25
            x=random.randint(r,SW-r)
            y=random.randint(r,SH-r)
            vx=random.randint(-3,3)
            vy=random.randint(-3,3)
            c = arcade.color.WHITE
            if vx==0:
                vx=random.randint(1,3)
            if vy==0:
                vy=random.randint(-3,-1)
            self.ball = Ball(x,y,vx,vy,r,c,)
            self.ball_list.append(self.ball)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_line(0, 500, 500, 500, arcade.color.WHITE, 25)
        arcade.draw_line(0, 0, 0, 500, arcade.color.WHITE, 25)
        arcade.draw_line(0, 0, 500, 0, arcade.color.WHITE, 25)
        arcade.draw_line(500, 0, 500, 500, arcade.color.WHITE, 25)
        #End line boarders
        arcade.draw_line(0,250,500,250,arcade.color.WHITE,15)
        #circle below
        arcade.draw_circle_outline(250,250,65,arcade.color.WHITE,15)
#goal top
        arcade.draw_line(150,500,150,400,arcade.color.WHITE,15)
        arcade.draw_line(143,400,350,400,arcade.color.WHITE,15)
        arcade.draw_line(350,500,350,393,arcade.color.WHITE,15)
#goal bot
        arcade.draw_line(150,0,150,107,arcade.color.WHITE,15)
        arcade.draw_line(150,100,350,100,arcade.color.WHITE,15)
        arcade.draw_line(350,0,350,107,arcade.color.WHITE,15)



        for item in(self.ball_list):
            item.draw_ball()
        # arcade.draw_circle_filled(self.x,self.y,20,arcade.color.ALIZARIN_CRIMSON)


    def on_update(self, dt):
        for item in (self.ball_list):
            item.update_ball()
        # self.x +=2
        # self.y +=2

def main():
    window = MyGame(SW,SH,"Soccer")
    arcade.run()

if __name__=="__main__":
    main()
