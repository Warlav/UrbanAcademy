import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGT = 600
SCREEN_TITLE = 'Pong Game'

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 1.0)


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()

if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGT, SCREEN_TITLE)
    arcade.run()