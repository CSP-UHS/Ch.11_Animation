import time
import arcade
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Radar Sweep Example"

CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2
SWEEP_LENGTH = 250


def on_draw(delta_time):

    on_draw.second += delta_time/10
    x_minute = SWEEP_LENGTH * math.sin(on_draw.minute) + CENTER_X
    y_minute = SWEEP_LENGTH * math.cos(on_draw.minute) + CENTER_Y

    x_hour =SWEEP_LENGTH/1.5 * math.sin(on_draw.hour) + CENTER_X
    y_hour = SWEEP_LENGTH/1.5 * math.cos(on_draw.hour) + CENTER_Y

    x_second = SWEEP_LENGTH * math.sin(on_draw.second) + CENTER_X
    y_second = SWEEP_LENGTH * math.cos(on_draw.second) + CENTER_Y

    arcade.start_render()
    arcade.draw_circle_filled(CENTER_X, CENTER_Y, SWEEP_LENGTH, arcade.color.WHITE)
    arcade.draw_text("XII", CENTER_X - 25, CENTER_Y + 200, arcade.color.BLACK, 36)  # 12
    arcade.draw_text("VI", CENTER_X - 15, CENTER_Y - 235, arcade.color.BLACK, 36)  # 6
    arcade.draw_text("IX", CENTER_X - 235, CENTER_Y - 20, arcade.color.BLACK, 36)  # 9
    arcade.draw_text("III", CENTER_X + 200, CENTER_Y - 20, arcade.color.BLACK, 36)  # 3

    arcade.draw_line(CENTER_X, CENTER_Y, x_minute, y_minute, arcade.color.RED, 8)
    arcade.draw_line(CENTER_X, CENTER_Y, x_hour, y_hour, arcade.color.BLUE, 8)
    arcade.draw_line(CENTER_X, CENTER_Y, x_second, y_second, arcade.color.ORANGE, 2)

    arcade.draw_circle_outline(CENTER_X, CENTER_Y, SWEEP_LENGTH,
                               arcade.color.BROWN_NOSE, 10)
    if on_draw.minute > 6.282:
        on_draw.minute = 0
        on_draw.hour += 6.282/60
    if on_draw.hour > 6.282:
        on_draw.hour = 0
    if on_draw.second > 6.282:
        on_draw.second = 0
        on_draw.minute += 6.282/60


second = time.strftime("%S")
hour = time.strftime("%I")
minute = time.strftime("%M")

on_draw.second = (6.282/60) * float(second)
on_draw.minute = (6.282/60) * float(minute) + on_draw.second/60
on_draw.hour = (6.282/12) * float(hour) + on_draw.minute/10


def main():

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_draw, 1 / 60)
    arcade.run()
    arcade.close_window()


if __name__ == "__main__":
    main()
