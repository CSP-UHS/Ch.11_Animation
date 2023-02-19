import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5
GRAVITY = 0.2

# just imagine the skaters pushing himself when he goes off-screen because I didn't have the patience to animate it
# on screen lol


class Skateboarder(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.textures = []
        for i in range(4):
            texture = arcade.load_texture(f"skateboarder{i}clear.png")
            self.textures.append(texture)
        self.texture = self.textures[0]
        self.set_position(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.velocity = 0
        self.pushing = False
        self.push_counter = 0
        self.push_duration = 0.7

    def update(self):
        self.center_y = (SCREEN_HEIGHT/2)+(SCREEN_HEIGHT/8)
        if self.pushing:
            if self.push_counter < self.push_duration * 60:
                self.velocity += MOVEMENT_SPEED * 2
                self.push_counter += 1
            else:
                self.pushing = False
                self.push_counter = 0
        else:
            self.velocity -= GRAVITY
        self.center_x += self.velocity
        if self.center_x < -300:
            self.center_x = -300
            self.velocity *= -1.005
        elif self.center_x > SCREEN_WIDTH:
            self.center_x = SCREEN_WIDTH
            self.velocity *= -1
        self.texture = self.textures[int(self.center_x // 20) % 4]


class Bird(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(f"smallmanakin.png")
        self.set_position(1000, 550)

    def update(self):
        if self.center_x < -2000:
            self.center_x = 2000
        self.center_x -= 10


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Skateboarder Racing a Car Through Paraíso")
        self.sprite_list = arcade.SpriteList()
        for i in range(200):
            filename = f"tree{random.randint(0,10)}.png"
            scale = random.randint(30, 50) / 100
            sprite = arcade.Sprite(filename, scale)
            sprite.center_x = random.randint(-3000, 3000)
            sprite.center_y = random.randint(340, 350)
            self.sprite_list.append(sprite)

        self.skateboarder = Skateboarder()

        self.background_color = arcade.color.SKY_BLUE

        self.bird = Bird()

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/6, SCREEN_WIDTH, 200, arcade.color.BATTLESHIP_GREY)
        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/40, SCREEN_WIDTH, 30,
                                     arcade.color_from_hex_string("5c595a"))
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.40, SCREEN_WIDTH, 106, arcade.color.AO)

        self.sprite_list.draw()

        self.bird.draw()

        self.skateboarder.draw()

    def on_update(self, delta_time):
        self.skateboarder.update()
        for sprite in self.sprite_list:
            if sprite.center_x < -3000:
                sprite.center_x = 3000
            sprite.center_x -= 15
        self.bird.update()


def main():
    window = MyGame()
    arcade.run()


if __name__ == "__main__":
    main()
