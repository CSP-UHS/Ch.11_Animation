import arcade
SW = 640
SH = 480

class MyGame(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.x = 320
        self.y = 240
    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.x,self.y,20,arcade.color.ALIZARIN_CRIMSON)

def main():
    window = MyGame(SW,SH,"Practice")
    arcade.run()

if __name__ == "__main__":
    main()