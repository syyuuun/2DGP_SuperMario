from pico2d import *

import game_world

class Fire:
    image = None
    def __init__(self, x = 800, y = 300, velocity = 1):
        if Fire.image == None:
            Fire.image = load_image("Resources/Mario/fire.png")        
        # fire position    
        self.x, self.y, self.velocity = x, y,velocity
        self.is_hit = False
    
    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        # fire position 
        if self.is_hit == True:
            game_world.remove_object(self)
        else:
            self.x += self.velocity

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self,other,group):
        if group == "fire:goombas" or group=="fire:troopas" or group == "fire:koopa":
            self.is_hit = True
        