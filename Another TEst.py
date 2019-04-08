import arcade
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Planets"

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
RADIANS_PER_FRAME = 0.02  # Speed of Sweep
SWEEP_LENGTH = 250  # Reach of spin


def on_draw(dt):
    on_draw.angle += RADIANS_PER_FRAME

    x = SWEEP_LENGTH * math.sin(on_draw.angle) + CENTER_X
    y = SWEEP_LENGTH * math.cos(on_draw.angle) + CENTER_Y


    arcade.start_render()
    arcade.draw_circle_filled(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 10, arcade.color.SUNGLOW)
    # arcade.draw_line(CENTER_X, CENTER_Y, x, y, arcade.color.WHITE, 4)
    # arcade.draw_circle_outline(CENTER_X, CENTER_Y, SWEEP_LENGTH, arcade.color.GREEN, 10)
    arcade.draw_circle_filled(x, y, 40, arcade.color.PURPLE)
    arcade.draw_circle_filled(x, y, 20, arcade.color.BLUE)


on_draw.angle = 0


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()
    arcade.close_window()


if __name__ == "__main__":
    main()
