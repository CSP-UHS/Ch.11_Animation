'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
import timeit
import time

screen_width = 650
screen_height = 650
paddle_height = 180
box_amount = 1

rand_one = random.randint(-10, 10)
rand_two = random.randint(-10, 10)

class Ball:
    def __init__(self, x, y, side, speed_x, speed_y):
        self.x = x
        self.y = y
        self.dx = side
        self.dy = side
        self.color = arcade.color.WHITE
        self.speed_x = speed_x
        self.speed_y = speed_y
        if self.speed_x == 0:
            self.speed_x = 1
        elif self.speed_y == 0:
            self.speed_y = 1

    def ball_draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, self.dx, self.dy, self.color)
        arcade.draw_rectangle_filled(15, screen_height / 2, 30, paddle_height, arcade.color.WHITE)
        arcade.draw_rectangle_filled(screen_width - 15, screen_height / 2, 30, paddle_height, arcade.color.WHITE)

    def update_ball(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.color = arcade.color.WHITE
        
        if self.x - (0.5 * self.dx) <= 30:
            if self.speed_x < 0:
                self.speed_x *= -1
        elif self.x + (0.5 * self.dx) >= screen_width - 30:
            if self.speed_x > 0:
                self.speed_x *= -1
        elif self.y - (0.5 * self.dy) <= 0:
            if self.speed_y < 0:
                self.speed_y *= -1
        elif self.y + (0.5 * self.dy) >= screen_height:
            if self.speed_y > 0:
                self.speed_y *= -1
                
        if self.y >= 415 and self.x - (0.5 * self.dx) <= 30:
            self.x = screen_width / 2
            self.y = screen_height / 2
            rand_one = random.randint(-10, 10)
            rand_two = random.randint(-10, 10)
            time.sleep(1)
            print("PLAYER TWO SCORED")
        elif self.y <= 235 and self.x - (0.5 * self.dx) <= 30:
            self.x = screen_width / 2
            self.y = screen_height / 2
            rand_one = random.randint(-10, 10)
            rand_two = random.randint(-10, 10)
            time.sleep(1)
            print("PLAYER TWO SCORED")
        elif self.y >= 415 and self.x + (0.5 * self.dx) >= screen_width - 30:
            self.x = screen_width / 2
            self.y = screen_height / 2
            time.sleep(1)
            print("PLAYER ONE SCORED")
        elif self.y <= 235 and self.x + (0.5 * self.dx) >= screen_width - 30:
            self.x = screen_width / 2
            self.y = screen_height / 2
            time.sleep(1)
            print("PLAYER ONE SCORED")

class Render(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.draw_time = 0
        
        self.frame_count = 0
        self.fps_start_timer = None
        self.fps = None

        self.box_list = []
        self.box_list.append(Ball(screen_width/2, screen_height/2, 25, rand_one, rand_two))

    def on_draw(self):
        start_time = timeit.default_timer()

        fps_calculation_freq = 60
        if self.frame_count % fps_calculation_freq == 0:
            if self.fps_start_timer is not None:
                total_time = timeit.default_timer() - self.fps_start_timer
                self.fps = fps_calculation_freq / total_time
            self.fps_start_timer = timeit.default_timer()
        self.frame_count += 1
        
        arcade.start_render()
        
        for i in range(len(self.box_list)):
            self.box_list[i].ball_draw()
            
        output = f"Drawing time: {self.draw_time:.3f}"
        arcade.draw_text(output, 32, screen_height - 50, arcade.color.WHITE, 18)

        if self.fps is not None:
            output = f"FPS: {self.fps:.0f}"
        arcade.draw_text(output, 32, screen_height - 75, arcade.color.WHITE, 18)
        self.draw_time = timeit.default_timer() - start_time

    def on_update(self, delta_time: float):
        start_time = timeit.default_timer()
        for i in range(len(self.box_list)):
            self.box_list[i].update_ball()
        self.processing_time = timeit.default_timer() - start_time

def main():
    window = Render(screen_height, screen_width, 'Pong Clone')
    arcade.run()

if __name__ == '__main__':
    main()

