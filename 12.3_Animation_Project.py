'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
SW=600
SH=400

class Plane:
    def __init__(self,x,y,dx,dy,w,c):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.w=w
        self.c=c

    def draw_plane(self):
        body_list = (self.x, self.y), (self.x - 20, self.y + 10), (self.x - 55, self.y + 20), (self.x - 120, self.y +
        20),(self.x - 150, self.y + 40), (self.x - 160, self.y + 40), (self.x - 160, self.y + 10), (self.x - 130, self.y - 5)\
        , (self.x - 20, self.y - 5)
        cockpit_list = (self.x - 20, self.y + 10), (self.x - 55, self.y + 10), (self.x - 55, self.y + 20)
        wing_list = (self.x - 60, self.y - 3), (self.x - 90, self.y), (self.x - 110, self.y + 8), (self.x - 120, self.y + 8),\
                    (self.x - 130, self.y - 3), (self.x - 60, self.y - 3)
        arcade.draw_polygon_filled(body_list, arcade.color.ARMY_GREEN)
        arcade.draw_polygon_filled(cockpit_list, arcade.color.LIGHT_BLUE)
        arcade.draw_polygon_filled(wing_list, arcade.color.DESERT)

    def update_plane(self):
        self.x+= self.dx
        self.y+= self.dy

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.plane = Plane(-40,200,3,0,20,arcade.color.ARMY_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.plane.draw_plane()

    def on_update(self, dt):
        self.plane.update_plane()

def main():
    window = MyGame(SW, SH, "Window")
    arcade.run()


if __name__ == "__main__":
    main()