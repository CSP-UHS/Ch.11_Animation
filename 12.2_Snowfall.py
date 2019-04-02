'''
SNOWFALL
--------
Try to create the snowfall animation by meeting
the following requirements:

1.) Create a 600 x 600 window with black background
2.) Window title equals "Snowfall"
3.) Crossbars 10 px wide. Snow must be outside!
4.) Make snowflake radius random between 1-3
5.) Randomly start snowflakes anywhere in the window.
6.) Random downward speed of -4 to -1
7.) Start snowflakes again at random x from 0-600 and random y from 600-700
8.) Generate 300 snowflakes
9.) Color snowflake #1 red just for fun.
10.) All other snowflakes should be white.


'''
import arcade

screen_width = 600
screen_height = 600
snowflakes = 300


class Snowflake:
	def __init__(self, pos_x, pos_y, radius, color):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius
		self.color = color

	def draw_snow(self):
		arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radius, self.color)

	def update_snow(self):
		pass  # Logic


class Snowfall(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		arcade.set_background_color(arcade.color.BLACK)
		self.snowflakelist = []
		for i in range(snowflakes):
			self.snowflake = Snowflake(300, 300, 3, arcade.color.RED)
			self.snowflakelist.append(self.snowflake)

	def on_draw(self):
		arcade.start_render()

	def update(self, dt):
		self.snowflake.update_snow()


def main():
	Snowfall(screen_width, screen_height, "Snowfall")
main()