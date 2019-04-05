import arcade
import random
import math

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Rocket Ship"


class Rocket:
    def __init__(self):
        self.x = 0
        self.y = 0

    def reset_pos(self):
        self.y = -50


class Fire:
    def __init_(self):
        self.x = 0
        self.y = 0


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.fire_list = None
        self.rocket_list = None

    def start_rocket(self):
        self.rocket_list = []
        rocket = Rocket()
        rocket.x = SCREEN_WIDTH/2
        rocket.y = SCREEN_HEIGHT/2
        rocket.speed = 200
        self.rocket_list.append(rocket)

    def start_fire(self):
        self.fire_list = []
        for i in range(25):
            fire = Fire()
            for rocket in self.rocket_list:
                fire.y = rocket.y
                fire.x = rocket.y
            fire.size = random.randrange(1, 40)
            fire.speed = 200
            fire.angle = random.uniform(math.pi, math.pi * 2)
            fire.color = self.fire_color()
            self.fire_list.append(fire)

    def fire_color(self):
        x = random.choice((arcade.color.RED, arcade.color.YELLOW, arcade.color.ORANGE))
        return x

    def on_draw(self):
        arcade.start_render()
        for rocket in self.rocket_list:
            tip_list = ((rocket.x-25, rocket.y+50), (rocket.x, rocket.y+75), (rocket.x+25, rocket.y+50))
            arcade.draw_rectangle_filled(rocket.x, rocket.y, 50, 100, arcade.color.WHITE)
            arcade.draw_polygon_filled(tip_list, arcade.color.WHITE)
            for fire in self.fire_list:
                arcade.draw_circle_filled(rocket.x, fire.y-50, fire.size, fire.color)

    def update(self, dt):
        for rocket in self.rocket_list:
            #  Move the rocket up
            rocket.y += rocket.speed * dt
            if rocket.y >= SCREEN_HEIGHT+50:
                rocket.reset_pos()
            self.start_fire()
        for fire in self.fire_list:
            fire.y -= fire.speed * dt


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.start_rocket()
    arcade.run()


if __name__ == "__main__":
    main()