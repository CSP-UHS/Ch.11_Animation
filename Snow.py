import arcade
import random

screen_width = 600
screen_height = 600
sprite_list = []
number_of_snow = 100


class Snow:
    def __init__(self, x, y, width, height, color, angle, fall_speed):
        self.pos_x = x
        self.pos_y = y
        self.height = height
        self.width = width
        self.color = color
        self.angle = angle
        self.fall_speed = fall_speed

    def draw_snow(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.color, self.angle)

    def update_snow(self):
        self.pos_y -= self.fall_speed
        self.angle += random.randrange(1, 5)

        # Teleports the snow to the top if it reaches the bottom
        if self.pos_y <= screen_height-screen_height-100:
            self.pos_y = screen_height + 10
            self.pos_x = random.randrange(0, screen_width)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GRAY)
        self.snowlist = []
        for i in range(number_of_snow):
            size = random.randrange(5, 10)
            self.snow = Snow(random.randrange(0, 1281), random.randrange(0, screen_height+200), size, size,
                             arcade.color.SNOW, 45, random.randrange(1, 3))
            self.snowlist.append(self.snow)

    def on_draw(self):
        arcade.start_render()
        # Put DRAWING CODE HERE
        for self.snow in self.snowlist:
            self.snow.draw_snow()

    def update(self, dt):
        for self.snow in self.snowlist:
            self.snow.update_snow()


def main():
    MyGame(screen_width, screen_height, "Snowing")
    arcade.run()


if __name__ == "__main__":
    main()
