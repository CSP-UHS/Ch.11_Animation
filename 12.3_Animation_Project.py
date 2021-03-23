"""
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

"""
import arcade
import random

SW = 660
SH = 600
target_right = 0
need_calc_right = True
target_left = 0
need_calc_left = False
rmove = 0
lmove = 0
lscore = 0
rscore = 0


class Ball:
    def __init__(self):
        self.x = 330
        self.y = 300
        self.radius = 10
        self.dx = 10
        self.dy = random.randint(-5, 5)
        if self.dy == 0:
            self.dy = 1
        self.color = arcade.color.WHITE

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def ball_update(self):
        self.x += self.dx
        if self.y - self.radius <= 0 or self.y + self.radius >= SH:
            self.dy = -self.dy
        self.y += self.dy


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 10
        self.color = (255, 255, 255)

    def paddle_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)

    def paddle_move_right(self, y, dy):
        global current_targ_right
        self.target = y
        self.dy = dy
        for i in range(60):
            if self.target >= 600 or self.target <= 0:
                self.dy = -self.dy
            self.target += self.dy
        current_targ_right = True
        if random.randint(0, 7) == 1:
            if random.randint(0, 1) == 0:
                return self.target - 30
            else:
                return self.target + 30
        else:
            return self.target


class Render(arcade.Window):
    def __init__(self, sc_width, sc_height, sc_title):
        super().__init__(sc_width, sc_height, sc_title)
        arcade.set_background_color((0, 0, 0))
        self.ball = [Ball()]
        self.paddle_left = Paddle(30, 300)
        self.paddle_right = Paddle(630, 300)

    def ball_goaway(self):
        global need_calc_left, need_calc_right, lscore, rscore
        if self.ball[0].x > SW:
            rscore += 1
            self.ball.remove(self.ball[0])
            self.ball.append(Ball())
            self.paddle_right.y, self.paddle_left.y = 300, 300
            need_calc_left, need_calc_right = False, True
        if self.ball[0].x < 0:
            lscore += 1
            self.ball.remove(self.ball[0])
            self.ball.append(Ball())
            self.paddle_right.y, self.paddle_left.y = 300, 300
            need_calc_left, need_calc_right = False, True

    def on_draw(self):
        arcade.start_render()
        self.ball[0].draw_ball()
        self.paddle_left.paddle_draw()
        self.paddle_right.paddle_draw()
        arcade.draw_text(str(lscore), 560, 550, arcade.color.WHITE, 30)
        arcade.draw_text(str(rscore), 50, 550, arcade.color.WHITE, 30)

    def on_update(self, delta_time: float):
        global need_calc_left, need_calc_right, rmove, lmove, lscore, rscore
        self.ball[0].ball_update()
        if self.ball[0].x - self.ball[0].radius < 35:
            if self.paddle_left.y + 25 > self.ball[0].y > self.paddle_left.y - 25:
                self.ball[0].dx *= -1
                if self.ball[0].dy > 0:
                    self.ball[0].dy = random.randint(1, 5)
                else:
                    self.ball[0].dy = random.randint(-5, -1)
        if self.ball[0].x + self.ball[0].radius > 625:
            if self.paddle_right.y + 25 > self.ball[0].y > self.paddle_right.y - 25:
                self.ball[0].dx *= -1
                if self.ball[0].dy > 0:
                    self.ball[0].dy = random.randint(1, 5)
                else:
                    self.ball[0].dy = random.randint(-5, -1)
        if self.ball[0].dx > 0:
            need_calc_left = True
            if need_calc_right:
                rmove = (self.paddle_right.paddle_move_right(self.ball[0].y, self.ball[0].dy)-self.paddle_right.y)/60
                need_calc_right = False
            self.paddle_right.y += rmove
        if self.ball[0].dx < 0:
            need_calc_right = True
            if need_calc_left:
                lmove = (self.paddle_left.paddle_move_right(self.ball[0].y, self.ball[0].dy)-self.paddle_left.y)/60
                need_calc_left = False
            self.paddle_left.y += lmove
        self.ball_goaway()


def main():
    Render(SW, SH, "Scuffed Pong")
    arcade.run()


if __name__ == "__main__":
    main()
