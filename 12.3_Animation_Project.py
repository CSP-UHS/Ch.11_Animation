'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade

screen_height = 600
screen_width = 600


class Rectangle:
	def __init__(self, pos_x, pos_y, width, height, color, rotate):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.width = width
		self.height = height
		self.color = color
		self.rotate = rotate

	def draw_rectangle(self):
		arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.color, self.rotate)

	def update_rectangle(self):
		# Logic goes here
		pass


class AnimationProject(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		self.rectangle_list = []
		for i in range(10):
			self.rectangle = Rectangle(screen_width/2, screen_height-15, screen_width, 30, arcade.color.PURPLE)
			self.rectangle_list.append(self.rectangle)

	def on_draw(self):
		for self.rectangle in self.rectangle_list:
			self.rectangle.draw_rectangle()

	def update(self, dt):
		pass
		for self.rectangle in self.rectangle_list:
			self.rectangle.update_rectangle()


def main():
	AnimationProject(screen_width, screen_height, "12.3 Animation Project")
	arcade.run()


if __name__ == "__main__":
	main()
