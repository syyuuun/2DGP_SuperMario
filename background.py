from pico2d import *

class BackGround:
    def __init__(self):
        self.image = load_image("Resources/Map/back_ground.png")

    def draw(self):
        self.image.draw(0, 600, 3280, 1200)
