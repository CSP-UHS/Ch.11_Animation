'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.
'''
import arcade
import random
SH=600
SW=600

class Star:
    def __init__(self, pos_x, pos_y, dx, dy, col):
        self.radius = random.randint(1, 5)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.col = col

    def update_star(self):
        self.pos_y = -self.pos_x
        self.pos_x += self.dx

    def draw_star(self):
        a = random.randint(0, 595)
        a2 = random.randint(400, 595)
        my_list = (
            (a, a2),
            (a + 2, a2 - 1),
            (a, a2 - 2),
            (a - 1, a2 - 5),
            (a - 2, a2 - 2),
            (a - 4, a2 - 1),
            (a - 2, a2),
            (a - 1, a2 + 2),
            (a, a2),
        )
        arcade.draw_polygon_filled(my_list, arcade.color.BUBBLES)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.CATALINA_BLUE)
        self.starlist = []
        for i in range(100):
            self.pos_x = random.randint(0, SW)
            self.pos_y = random.randint(200, SH)
            self.star = Star(self.pos_x, self.pos_y,1,3, arcade.color.BUBBLES) #put in correct numbers
            self.starlist.append(self.star)
    def on_draw(self):
        arcade.start_render()
        for item in self.starlist:
            item.draw_star()
        arcade.draw_lrtb_rectangle_filled(0,600,200,0, arcade.color.AO) # GRASS
        arcade.draw_triangle_filled(100, 200, 300, 400, 600, 200, arcade.color.EBONY) #middle mountian
        arcade.draw_triangle_filled(400, 200, 600, 350, 600, 200, arcade.color.DARK_GRAY)  # right mountian
        arcade.draw_triangle_filled(0,200, 0, 400, 500, 200, arcade.color.DIM_GRAY) #left mountian
    def on_update(self, dt):
        for item in self.starlist:
            item.update_star()
def main():
    window = MyGame(SH,SW, "SnowFall")
    arcade.run()
if __name__== "__main__":
    main()
main()
