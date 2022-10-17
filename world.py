from pico2d import *

class World:
    def __init__(self):
        self.image = load_image("Resources/Map/World1-1.png")

    def draw(self):
       self.image.draw(3280//2, 232//2)
