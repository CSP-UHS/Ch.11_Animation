import arcade
import random

# arcade.open_window(600,600, "lol")
# arcade.set_background_color(arcade.color.WHITE)
# arcade.start_render()
#
# for i in range(20):
#     a = random.randint(10,300)
#     a2 = random.randint(10,300)
#     my_list = (
#         (a, a2),
#         (a+2, a2-1),
#         (a, a2-2),
#         (a-1, a2-5),
#         (a-2, a2-2),
#         (a-4, a2-1),
#         (a-2, a2),
#         (a-1, a2+2),
#         (a, a2),
#     )
#
#     arcade.draw_polygon_filled(my_list, arcade.color.BLACK)
#
# arcade.finish_render()
# arcade.run()

import arcade
import random

class snow_ball:
    def __init__(self, pos_x, pos_y,dx, dy, col):
        self.radius = random.randint(1, 3)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dy = dy
        self.dx = dx
        self.col = col

    def draw_ball(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.col)


    def update_ball(self):
        self.pos_y = -self.pos_x
        self.pos_x += self.dx


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.snowlist = []
        for i in range(300):
            self.snow_ball = snow_ball(random.randint(100, 500),random.randint(100,590),1,1, arcade.color.WHITE)
            self.snowlist.append(self.snow_ball)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(300,300,10,600,arcade.color.RED_BROWN) # Y
        arcade.draw_rectangle_filled(300,300,600,10, arcade.color.RED_BROWN) # X
        for item in self.snowlist:
            item.draw_ball()

    def on_update(self, dt):
        for item in self.snowlist:
            item.update_ball()

def main():
    SH = 600
    SW = 600
    window = MyGame(SH,SW, "SnowFall")
    arcade.run()

main()
