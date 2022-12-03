from pico2d import *

import game_world

import server

class Fire:
    image = None
    def __init__(self, x = 800, y = 300, velocity = 1):
        if Fire.image == None:
            Fire.image = load_image("Resources/Mario/fire.png")        
        
        # fire position    
        self.x, self.y, self.velocity = x, y, velocity
        self.is_hit = False
        self.sx, self.sy = 0, 0
    
    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        if False == self.is_hit:
            self.image.draw(self.sx,self.sy)
            #draw_rectangle(*self.get_bb())

    def update(self):
        if self.is_hit == False:
            self.x += self.velocity
        else:
            game_world.remove_object(self)

    def get_bb(self):
        return self.sx - 10, self.sy - 10, self.sx + 10, self.sy + 10

    def handle_collision(self,other,group):
        if group == "fire:goombas":
            self.is_hit = True
        elif group == "fire:troopas":
            self.is_hit = True
        elif group == "fire:koopa":
            self.is_hit = True
        