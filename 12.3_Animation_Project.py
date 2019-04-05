'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade

screen_height = 600
screen_width = 600
amount_stars = 5


class Star:
    def __init__(self, pos_x, pos_y, width, height, color, rotate):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.rotate = rotate

    def draw_star(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.color, self.rotate)

    def update_star(self):
        self.pos_y -= 1


class AnimationProject(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.star_list = []
        for i in range(amount_stars):
            self.star = Star(screen_width/2, screen_height/2, 15, 30, arcade.color.PURPLE, 0)
            self.star_list.append(self.star)

    def on_draw(self):
        for self.star in self.star_list:
            self.star.draw_star()

    def update(self, dt):
        for self.star in self.star_list:
            self.star.update_star()


def main():
    AnimationProject(screen_width, screen_height, "12.3 Animation Project")
    arcade.run()


if __name__ == "__main__":
    main()
