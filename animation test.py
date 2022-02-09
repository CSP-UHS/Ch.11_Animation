import arcade
SW=640
SH=480
class Balls():
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.dx=dx
        self.dy=dy
        self.rad=rad
        self.col=col
    def draw_balls(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.rad,self.col)
    def update_balls(self):
        self.pos_x+=self.dx
        self.pos_y+=self.dy
        if self.pos_x>SW-self.rad or self.pos_x<self.rad:
            self.dx*=-1
        if self.pos_y > SH - self.rad or self.pos_y < self.rad:
            self.dy *= -1








class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.balls=Balls(320,240,3,2,15,arcade.color.AFRICAN_VIOLET)
    def on_draw(self):
        arcade.start_render()
        self.balls.draw_balls()
    def on_update(self, dt):
        self.balls.update_balls()
def myprogram():
    window=MyGame(SW,SH,"Window")
    arcade.run()
if __name__=="__main__":
    myprogram()
