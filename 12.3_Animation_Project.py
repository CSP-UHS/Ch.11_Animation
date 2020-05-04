'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.
'''
import arcade
import random
SH=600
SW=600
# class Star:
#     def __init__(self, pos_x, pos_y, dx, dy, col):
#         self.radius = random.randint(1, 5)
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.dx = dx
#         self.dy = dy
#         self.col = col
#     def update_star(self):
#         self.pos_y = -self.pos_x
#         self.pos_x += self.dx
#         if self.pos_y<400:
#             self.pos_x=random.randint(0,SW)
#             self.pos_y= random.randint(SH, SW+100)
#     def draw_star(self):
#         # a = random.randint(0, 595)
#         # a2 = random.randint(400, 595)
#         my_list = (
#             (self.pos_x, self.pos_y),
#             (self.pos_x + 2, self.pos_y - 1),
#             (self.pos_x, self.pos_y - 2),
#             (self.pos_x - 1, self.pos_y - 5),
#             (self.pos_x - 2, self.pos_y - 2),
#             (self.pos_x - 4, self.pos_y - 1),
#             (self.pos_x - 2, self.pos_y),
#             (self.pos_x - 1, self.pos_y + 2),
#             (self.pos_x, self.pos_y),
#         )
#         arcade.draw_polygon_filled(my_list, arcade.color.BLACK)
#
# class MyGame(arcade.Window):
#     def __init__(self, width, height, title):
#         super().__init__(width, height, title)
#         arcade.set_background_color(arcade.color.WHITE)
#         self.starlist = []
#         for i in range(5):
#             self.pos_x = random.randint(0, SW)
#             self.pos_y = random.randint(400, SH)
#             self.color = arcade.color.BLACK
#             self.star = Star(self.pos_x, self.pos_y, 1, 3, self.color)
#             self.starlist.append(self.star)
#
#     def on_draw(self):
#         arcade.start_render()
#         # arcade.draw_lrtb_rectangle_filled(0,600,200,0, arcade.color.AO) # GRASS
#         # arcade.draw_triangle_filled(100, 200, 300, 400, 600, 200, arcade.color.EBONY) #middle mountian
#         # arcade.draw_triangle_filled(400, 200, 600, 350, 600, 200, arcade.color.DARK_GRAY)  # right mountian
#         # arcade.draw_triangle_filled(0,200, 0, 400, 500, 200, arcade.color.DIM_GRAY) #left mountian
#         for item in self.starlist:
#             item.draw_star()
#     def on_update(self, dt):
#         for item in self.starlist:
#             item.update_star()
# def main():
#     window = MyGame(SH,SW, "SnowFall")
#     arcade.run()
# if __name__== "__main__":
#     main()
# main()

ST=300

class Star:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.radius = random.randint(1, 5)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def update_star(self):
        self.pos_y -= 1
        self.pos_x -= 1

        if self.pos_y<200:
            self.pos_x=random.randint(0,SW)
            self.pos_y= random.randint(SH, SW+100)

    def draw_star(self):
        arcade.draw_circle_filled(self.pos_x,self.pos_y,self.radius,self.col)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.CATALINA_BLUE)
        self.starlist_1 = []
        self.starlist_2 = []
        self.starlist_3 = []
        for i in range(ST//3):
            self.pos_x = random.randint(0, 595)
            self.pos_y = random.randint(100, 595)
            self.rad = 1
            self.star = Star(self.pos_x, self.pos_y, 7, 5, self.rad, arcade.color.BUBBLES) #put in correct numbers
            self.starlist_1.append(self.star)
        for i in range(ST//3):
            self.pos_x = random.randint(0, 595)
            self.pos_y = random.randint(100, 595)
            self.rad = 7
            self.star = Star(self.pos_x, self.pos_y, 4, 3, self.rad, arcade.color.BUBBLES) #put in correct numbers
            self.starlist_2.append(self.star)
        for i in range(ST//3):
            self.pos_x = random.randint(0, 595)
            self.pos_y = random.randint(100, 595)
            self.rad = 20
            self.star = Star(self.pos_x, self.pos_y, 3, 1, self.rad, arcade.color.BUBBLES) #put in correct numbers
            self.starlist_3.append(self.star)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_triangle_filled(100, 200, 300, 400, 600, 200, arcade.color.EBONY)  # middle mountian
        for item in self.starlist_1:
            item.draw_star()
        arcade.draw_triangle_filled(400, 200, 600, 350, 600, 200, arcade.color.DARK_GRAY)  # right mountian
        arcade.draw_triangle_filled(0,200, 0, 400, 500, 200, arcade.color.DIM_GRAY) #left mountian
        for item in self.starlist_2:
            item.draw_star()
        arcade.draw_lrtb_rectangle_filled(0, 600, 200, 0, arcade.color.AO)  # GRASS
        for item in self.starlist_3:
            item.draw_star()

    def on_update(self, dt):
        for item in self.starlist_1:
            item.update_star()
        for item in self.starlist_2:
            item.update_star()
        for item in self.starlist_3:
            item.update_star()

def main():
    window = MyGame(SH,SW, "SnowFall")
    arcade.run()
if __name__== "__main__":
    main()
main()


