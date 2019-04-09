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
RADIANS_PER_FRAME = .00020833
RADIANS_PER_FRAME_2 = RADIANS_PER_FRAME/12
SWEEP_LENGTH = 250


def on_draw(delta_time):
    on_draw.angle += (delta_time/60)/12
    on_draw.angle_2 += RADIANS_PER_FRAME_2

    # Big Hand
    x = SWEEP_LENGTH * math.sin(on_draw.angle) + CENTER_X
    y = SWEEP_LENGTH * math.cos(on_draw.angle) + CENTER_Y
    # Little Hand
    x_2 = SWEEP_LENGTH/1.5 * math.sin(on_draw.angle_2) + CENTER_X
    y_2 = SWEEP_LENGTH/1.5 * math.cos(on_draw.angle_2) + CENTER_Y

    arcade.start_render()
    arcade.draw_text("12", CENTER_X - 25, CENTER_Y + 200, arcade.color.WHITE, 36)  # 12
    arcade.draw_text("6", CENTER_X - 15, CENTER_Y - 235, arcade.color.WHITE, 36)  # 6
    arcade.draw_text("9", CENTER_X - 235, CENTER_Y - 20, arcade.color.WHITE, 36)  # 9
    arcade.draw_text("3", CENTER_X + 200, CENTER_Y - 20, arcade.color.WHITE, 36)  # 3
    arcade.draw_line(CENTER_X, CENTER_Y, x, y, arcade.color.OLIVE, 8)
    arcade.draw_line(CENTER_X, CENTER_Y, x_2, y_2, arcade.color.GRAY, 8)
    arcade.draw_circle_outline(CENTER_X, CENTER_Y, SWEEP_LENGTH,
                               arcade.color.DARK_GREEN, 10)
    print(on_draw.angle)


hour = time.strftime("%I")
minute = time.strftime("%M")
second = time.strftime(".%S")
if float(hour) == 12:
    hour = "11"
on_draw.angle_2 = float(hour) * .569
on_draw.angle = float(minute) + (float(second)/60) * .105
numbers = ["12", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()
    arcade.close_window()


if __name__ == "__main__":
    main()
