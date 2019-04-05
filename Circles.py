import random
import arcade
import math

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN_TITLE = "Circles"
AMOUNT_OF_CIRCLES = 50
FULLSCREEN = False  # True or False


class Circle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = circle_color()

    def reset_pos(self):
        self.y = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT + 100)
        self.x = random.randrange(SCREEN_WIDTH)
        self.color = circle_color()


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        if FULLSCREEN is True:
            self.set_fullscreen(not self.fullscreen)
        self.circle_list = None

    def start_circle(self):
        self.circle_list = []
        for i in range(AMOUNT_OF_CIRCLES):
            circle = Circle()
            # Stars start in random position
            circle.x = random.randrange(SCREEN_WIDTH)
            circle.y = random.randrange(SCREEN_HEIGHT + 200)
            circle.size_change = 2
            circle.size = random.randrange(1, 21)
            circle.speed = random.randrange(20, 40)
            # Sways circles
            circle.angle = random.uniform(math.pi, math.pi * 2)
            circle.color = circle_color()

            self.circle_list.append(circle)

    def on_draw(self):
        arcade.start_render()
        for circle in self.circle_list:
            arcade.draw_circle_filled(circle.x, circle.y, circle.size, circle.color)

    def update(self, dt):
        for circle in self.circle_list:
            circle.y -= circle.speed * dt
            # Adjusts size
            if circle.size > 20:
                circle.size_change = -6
            if circle.size < 1:
                circle.size_change = 4
            circle.size += circle.size_change * dt

            if circle.y < - 20:
                circle.reset_pos()
            # Sways circle around in a circle
            circle.y += circle.speed * math.sin(circle.angle) * dt
            circle.y += circle.speed * math.sin(circle.angle) * dt
            circle.angle += 1 * dt


def circle_color():
    # Returns a random rainbow color
    x = random.choice((arcade.color.RED, arcade.color.YELLOW, arcade.color.ORANGE,
                        arcade.color.GREEN, arcade.color.BLUE, arcade.color.PURPLE))
    return x


def main():
    if FULLSCREEN is False:
        global SCREEN_HEIGHT, SCREEN_WIDTH
        SCREEN_HEIGHT = 720
        SCREEN_WIDTH = 1080
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_circle()
    arcade.run()


if __name__ == "__main__":
    main()
