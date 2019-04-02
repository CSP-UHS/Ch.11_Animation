'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade

screen_height = 600
screen_width = 600


class AnimationProject(arcade.Window):
	def __init__(self, width, height, title):
		super().__init__(width, height, title)

	def on_draw(self):
		pass

	def update(self, dt):
		pass


def main():
	AnimationProject(screen_width, screen_height, "12.3 Animation Project")
	arcade.run()


if __name__ == "__main__":
	main()
