import arcade
import random

# arcade.open_window(600,600, "lol")
# arcade.set_background_color(arcade.color.WHITE)
# arcade.start_render()
#
# a = 14
# a2 = 20
# my_list = (
#     (a, a2),
#     (18, 18),
#     (14, 16),
#     (12, 10),
#     (10, 16),
#     (6, 18),
#     (10, 20),
#     (12, 26),
#     (14, 20),
# )
# arcade.draw_polygon_filled(my_list, arcade.color.BLACK)
#
# arcade.finish_render()
# arcade.run()

arcade.open_window(600,600, "lol")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

a = random.randint(10,300)
a2 = random.randint(10,300)
my_list = (
    (a, a2),
    (a+2, a2-1),
    (a, a2-2),
    (a-1, a2-5),
    (a-2, a2-2),
    (a-4, a2-1),
    (a-2, a2),
    (a-1, a2+2),
    (a, a2),
)

arcade.draw_polygon_filled(my_list, arcade.color.BLACK)

arcade.finish_render()
arcade.run()

