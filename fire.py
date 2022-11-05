from pico2d import *

import game_world

class Fire:
    image = None

    def __init__(self, x = 800, y = 300, velocity = 1):
        if Fire.image == None:
            Fire.image = load_image("Resources/Mario/fire.png")
        
        self.x, self.y, self.velocity = x, y,velocity
    
    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 20 or self.x > 800 -20:
            game_world.remove_object(self)