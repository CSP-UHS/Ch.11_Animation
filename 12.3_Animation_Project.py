'''
EPILESY WARNING!!!!!
'''
import arcade
import random
sw = 800
sh = 600
color1 = random.randint(0, 255)
color2 = random.randint(0, 255)
color3 = random.randint(0, 255)
class Star:
    def __init__(self,pos_x,pos_y,dx,dy,rad,col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col
        self.yes = True

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)
    def update_ball(self):
        self.pos_x += self.dx
        self.pos_y += self.dy



class Planet(Star):
    #def check(self):
        #if self.yes == True:
            #self.yes = False
    def explode(self):
        if self.pos_x == sw/2:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.ORANGE)
            arcade.draw_text("BOOM!", 300, 300, arcade.color.BLACK, 40, 0, "left", "arial")
        if self.pos_x == sw or self.pos_x == sw-sw:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.BLACK)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+1 or self.pos_x == -1:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.WHITE)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+2 or self.pos_x == -2:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.GREEN)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+3 or self.pos_x == -3:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.PURPLE)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+4 or self.pos_x == -4:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.RED)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+5 or self.pos_x == -5:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.PINK)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+6 or self.pos_x == -6:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.BLUE)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+7 or self.pos_x == -7:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.BROWN)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+8 or self.pos_x == -8:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.ASH_GREY)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+9 or self.pos_x == -9:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.GOLD)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+10 or self.pos_x == -10:
            arcade.draw_lrtb_rectangle_filled(1, sw, sh, 1, arcade.color.TEA_GREEN)
            arcade.draw_ellipse_filled(400,300,50,90,arcade.color.ORANGE,45)
        if self.pos_x == sw+11 or self.pos_x == -11:
            arcade.close_window()




class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.ball_list = []
        for i in range(1000):
            self.ball_list.append(Star(random.randint(-1000,800),random.randint(1,600),random.randint(1,5),0,5,arcade.color.WHITE))
        self.panet_list = []
        self.panet_list.append(Planet(5,sh/2,1,0,50,arcade.color.ORANGE))
        self.panet_list.append(Planet(sw-5,sh/2,-1,0,40,arcade.color.BLUE))
        self.t_list = []
        for i in range(20):
            self.t_list.append((Planet(random.randint(1,800),random.randint(1,600),random.randint(-10,10),random.randint(-10,10),random.randint(1,20),[color1,color2,color3])))

    def on_draw(self):
        arcade.start_render()
        for i in range(len(self.ball_list)):
            self.ball_list[i].draw_ball()
        for i in range(len(self.panet_list)):
            self.panet_list[i].draw_ball()
            self.panet_list[i].explode()

        for i in range(len(self.t_list)):
            self.t_list[i].draw_ball()

    def on_update(self, dt):
        for i in range(len(self.ball_list)):
            self.ball_list[i].update_ball()
        for i in range(len(self.panet_list)):
            self.panet_list[i].update_ball()
            self.panet_list[i].explode()
        for i in range(len(self.t_list)):
            self.t_list[i].update_ball()


def myprogram():
    window = MyGame(sw,sh,"A Starry Collision")
    arcade.run()

if __name__ == '__main__':
    myprogram()