'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''

import arcade
import random

class Pokeball:
    def __init__(self,x,y,rad,direction,spin):
        self.x = x
        self.y = y
        self.rad = rad
        self.direction = direction
        self.spin = spin
    def draw_pokeball(self):
        arcade.draw_ellipse_filled(self.x,self.y-self.rad/1.05,self.rad,self.rad/10,arcade.color.SMOKY_BLACK)
        arcade.draw_circle_outline(self.x,self.y,self.rad,arcade.color.BLACK,self.rad/13.33)
        arcade.draw_circle_filled(self.x, self.y, self.rad, arcade.color.WHITE)
        arcade.draw_arc_filled(self.x,self.y,self.rad,self.rad,arcade.color.RED,self.direction,self.direction+180)
        arcade.draw_rectangle_filled(self.x,self.y,self.rad*2,self.rad/10,arcade.color.BLACK,self.direction)
        arcade.draw_circle_filled(self.x,self.y,self.rad/4,arcade.color.BLACK)
        arcade.draw_circle_filled(self.x,self.y,self.rad/6,arcade.color.WHITE)
        arcade.draw_circle_outline(self.x,self.y,self.rad/10,arcade.color.BLACK,self.rad/35)
        #arcade.draw_arc_outline(self.x-self.rad/3,self.y-self.rad/1.75,self.rad/1.5,self.rad/5,arcade.color.LIGHT_GRAY,180,360,self.rad/15,-25)
    def update_pokeball(self):
        self.direction+=self.spin

class Cloud:
    def __init__(self,x,y,dx,rad):
        self.x = x
        self.y = y
        self.dx = dx
        self.rad = rad
    def draw_cloud(self):
        arcade.draw_circle_filled(self.x,self.y,self.rad,arcade.color.WHITE_SMOKE)
        arcade.draw_circle_filled(self.x+self.rad/1.5,self.y,self.rad,arcade.color.WHITE_SMOKE)
        arcade.draw_circle_filled(self.x+self.rad/0.75, self.y, self.rad, arcade.color.WHITE_SMOKE)
        arcade.draw_circle_filled(self.x+self.rad/2, self.y+self.rad/2, self.rad, arcade.color.WHITE_SMOKE)
        arcade.draw_circle_filled(self.x+self.rad, self.y+self.rad/2, self.rad, arcade.color.WHITE_SMOKE)
    def update_cloud(self):
        self.x+=self.dx
        if self.x+self.rad/0.75+self.rad <= 0:
            self.x=600
            self.y=random.randrange(350,580)
            self.dx = random.randrange(-4,0)

class Tree:
    def __init__(self,x,y,dx,rad):
        self.x = x
        self.y = y
        self.dx = dx
        self.rad = rad
    def draw_tree(self):
        arcade.draw_rectangle_filled(self.x,self.y,self.rad/3,self.rad*2,arcade.color.DARK_BROWN)
        arcade.draw_circle_filled(self.x-self.rad/3,self.y+self.rad,self.rad/3,arcade.color.APPLE_GREEN)
        arcade.draw_circle_filled(self.x+self.rad/3,self.y+self.rad,self.rad/3,arcade.color.APPLE_GREEN)
        arcade.draw_circle_filled(self.x, self.y + self.rad*1.35, self.rad/3, arcade.color.APPLE_GREEN)
    def update_tree(self):
        self.x+=self.dx
        if self.x <= 0:
            self.x = 600
            self.dx = random.randrange(-4,0)
            self.rad = random.randrange(50,151)

class Pokemon(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_SKY_BLUE)
        self.pokeball = Pokeball(300,250,150,0,-4)
        self.cloud_list = []
        self.tree_list = []
        for i in range(random.randrange(3,9)):
            self.cloud = Cloud(random.randrange(0,600),random.randrange(350,580),random.randrange(-4,0),20)
            self.cloud_list.append(self.cloud)
        for i in range(random.randrange(1,4)):
            self.tree = Tree(random.randrange(0, 601), 225, random.randrange(-4, 0), random.randrange(50, 151))
            self.tree_list.append(self.tree)
    def on_draw(self):
        arcade.start_render()
        for item in self.cloud_list:
            item.draw_cloud()
        for item in self.tree_list:
            item.draw_tree()
        arcade.draw_lrtb_rectangle_filled(0,600,175,0,arcade.color.DARK_PASTEL_GREEN)
        self.pokeball.draw_pokeball()
    def on_update(self, dt):
        self.pokeball.update_pokeball()
        for item in self.cloud_list:
            item.update_cloud()
        for item in self.tree_list:
            item.update_tree()

def main():
    window = Pokemon(600, 600, "Pokemon")
    arcade.run()

main()