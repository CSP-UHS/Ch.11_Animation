"""
This animation example shows how perform a radar sweep animation.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.radar_sweep
"""
import arcade
import math
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Radar Sweep Example"

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
RADIANS_PER_FRAME = 0.01
RADIANS_PER_FRAME_2 = RADIANS_PER_FRAME/12
SWEEP_LENGTH = 250



def on_draw(delta_time):
    on_draw.angle += RADIANS_PER_FRAME
    on_draw.angle_2 += RADIANS_PER_FRAME_2

    # Big Hand
    x = SWEEP_LENGTH * math.sin(on_draw.angle) + CENTER_X
    y = SWEEP_LENGTH * math.cos(on_draw.angle) + CENTER_Y
    # Little Hand
    x_2 = SWEEP_LENGTH/1.5 * math.sin(on_draw.angle_2) + CENTER_X
    y_2 = SWEEP_LENGTH/1.5 * math.cos(on_draw.angle_2) + CENTER_Y

    arcade.start_render()
    arcade.draw_text("XII", CENTER_X - 25, CENTER_Y + 200, arcade.color.WHITE, 36)  # 12
    arcade.draw_text("VI", CENTER_X - 15, CENTER_Y - 235, arcade.color.WHITE, 36)  # 6
    arcade.draw_text("IX", CENTER_X - 235, CENTER_Y - 20, arcade.color.WHITE, 36)  # 9
    arcade.draw_text("III", CENTER_X + 200, CENTER_Y - 20, arcade.color.WHITE, 36)  # 3
    arcade.draw_line(CENTER_X, CENTER_Y, x, y, arcade.color.OLIVE, 4)
    arcade.draw_line(CENTER_X, CENTER_Y, x_2, y_2, arcade.color.GRAY, 4)
    arcade.draw_circle_outline(CENTER_X, CENTER_Y, SWEEP_LENGTH,
                               arcade.color.DARK_GREEN, 10)
    print(on_draw.angle_2)


hour = time.strftime("%I")
minute = time.strftime("%M")
on_draw.angle_2 = float(hour) * .5
on_draw.angle = float(minute) * .5
numbers = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1 / 80)
    arcade.run()
    arcade.close_window()


if __name__ == "__main__":
    main()
