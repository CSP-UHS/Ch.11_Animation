'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random

SW = 600
SH = 600
color = arcade.color.GREEN
rad = 5
col_list = [0]


class Ball:
    def __init__(self, x: int, y, dx, dy, r, c):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.r = r
        self.c = c
        self.collisions = 0

    def draw_ball(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, self.c)

    def update_ball(self):
        self.x += self.dx
        self.y += self.dy

        if 250 <= self.x <= 350 and self.y - rad <= 250 <= self.y + rad:
            self.dy *= -1
            #print("1")
            self.collisions += 1
        elif 200 <= self.x <= 400 and self.y - rad <= 200 <= self.y + rad:
            self.dy *= -1
            #print("2")
            self.collisions += 1
        elif 150 <= self.x <= 450 and self.y - rad <= 150 <= self.y + rad:
            self.dy *= -1
            #print("3")
            self.collisions += 1
        elif 100 <= self.x <= 500 and self.y - rad <= 100 <= self.y + rad:
            self.dy *= -1
            #print("4")
            self.collisions += 1
        elif 50 <= self.x <= 550 and self.y - rad <= 50 <= self.y + rad:
            self.dy *= -1
            #print("5")
            self.collisions += 1
        elif 200 <= self.x <= 350 and self.y - rad <= 350 <= self.y + rad:
            self.dy *= -1
            #print("6")
            self.collisions += 1
        elif 150 <= self.x <= 400 and self.y - rad <= 400 <= self.y + rad:
            self.dy *= -1
            #print("7")
            self.collisions += 1
        elif 100 <= self.x <= 450 and self.y - rad <= 450 <= self.y + rad:
            self.dy *= -1
            #print("8")
            self.collisions += 1
        elif 50 <= self.x <= 500 and self.y - rad <= 500 <= self.y + rad:
            self.dy *= -1
            #print("9")
            self.collisions += 1
        elif 0 <= self.x <= 550 and self.y - rad <= 550 <= self.y + rad:
            self.dy *= -1
            #print("10")
            self.collisions += 1
        elif 0 <= self.x <= 50 and self.y - rad <= 500 <= self.y + rad:
            self.dy *= -1
            #print("11")
            self.collisions += 1
        elif 250 <= self.y <= 350 and self.x + rad >= 350 >= self.x - rad:
            self.dx *= -1
            #print("12")
            self.collisions += 1
        elif 200 <= self.y <= 400 and self.x + rad >= 400 >= self.x - rad:
            self.dx *= -1
            #print("13")
            self.collisions += 1
        elif 150 <= self.y <= 450 and self.x + rad >= 450 >= self.x - rad:
            self.dx *= -1
            #print("14")
            self.collisions += 1
        elif 100 <= self.y <= 500 and self.x + rad >= 500 >= self.x - rad:
            self.dx *= -1
            #print("15")
            self.collisions += 1
        elif 50 <= self.y <= 550 and self.x + rad >= 550 >= self.x - rad:
            self.dx *= -1
            #print("16")
            self.collisions += 1
        elif 200 <= self.y <= 350 and self.x + rad >= 200 >= self.x - rad:
            self.dx *= -1
            #print("17")
            self.collisions += 1
        elif 150 <= self.y <= 400 and self.x + rad >= 150 >= self.x - rad:
            self.dx *= -1
            #print("18")
            self.collisions += 1
        elif 100 <= self.y <= 450 and self.x + rad >= 100 >= self.x - rad:
            self.dx *= -1
            #print("19")
            self.collisions += 1
        elif 50 <= self.y <= 500 and self.x + rad >= 50 >= self.x - rad:
            self.dx *= -1
            #print("20")
            self.collisions += 1
        elif 0 <= self.y <= 575 and self.x + rad >= 0 >= self.x - rad:
            print(len(col_list))

            if self.collisions != col_list[len(col_list)-1]:
                col_list.append(self.collisions)
                print("Collisions: ", col_list[1:])



class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.balllist = []
        for i in range(100):
            x_loc = random.randrange(256,345)
            y_loc = random.randrange(256,345)
            x_velocity = random.randrange(-5,6)
            y_velocity = random.randrange(-5,6)
            self.ball = Ball(x_loc, y_loc, x_velocity, y_velocity, rad, (random.randint(0,256),random.randint(0,256),random.randint(0,256)))
            self.balllist.append(self.ball)
        #print("X Location: ", x_loc)
        #print("Y Location: ", y_loc)
        #print("X Velocity:",x_velocity)
        #print("Y Velocity:",y_velocity)
        collisions = 0

    def on_draw(self):
        arcade.start_render()
        for ball in self.balllist:
            ball.draw_ball()
        arcade.draw_line(250, 250, 350, 250, color, 1)
        arcade.draw_line(350, 250, 350, 350, color, 1)
        arcade.draw_line(350, 350, 200, 350, color, 1)
        arcade.draw_line(200, 350, 200, 200, color, 1)
        arcade.draw_line(200, 200, 400, 200, color, 1)
        arcade.draw_line(400, 200, 400, 400, color, 1)
        arcade.draw_line(400, 400, 150, 400, color, 1)
        arcade.draw_line(150, 400, 150, 150, color, 1)
        arcade.draw_line(150, 150, 450, 150, color, 1)
        arcade.draw_line(450, 150, 450, 450, color, 1)
        arcade.draw_line(450, 450, 100, 450, color, 1)
        arcade.draw_line(100, 450, 100, 100, color, 1)
        arcade.draw_line(100, 100, 500, 100, color, 1)
        arcade.draw_line(500, 100, 500, 500, color, 1)
        arcade.draw_line(500, 500, 50, 500, color, 1)
        arcade.draw_line(50, 500, 50, 50, color, 1)
        arcade.draw_line(50, 50, 550, 50, color, 1)
        arcade.draw_line(550, 50, 550, 550, color, 1)
        arcade.draw_line(550, 550, 0, 550, color, 1)
        arcade.draw_line(0, 500, 50, 500, color, 1)

    def on_update(self, dt):
        for ball in self.balllist:
            ball.update_ball()

def main():
    MyGame(SW, SH, "Maze")
    arcade.run()


if __name__ == "__main__":
    main()
