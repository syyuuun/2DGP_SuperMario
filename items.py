from pico2d import *
import game_world
from random import randint

import server

class Mushroom:
    def __init__(self,x = 0, y = 0):
        self.image = load_image("Resources/Items/mushroom.png")
        self.x, self.y =x, y
        self.is_collision = False
        self.sx,self.sy = 0, 0
    def update(self):
        pass
    
    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(self.sx,self.sy)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.sx-8,self.sy-8,self.sx+8,self.sy+8
    
    def handle_collision(self,other,group):
        if group == "mario:mushrooms":
            self.is_collision = True
            game_world.remove_object(self)

class FireFlower:
    def __init__(self, x = 0, y = 0):
        self.image = load_image("Resources/Items/fire_flower.png")
        self.x, self.y = x, y
        self.is_collision = False
        self.sx, self.sy = 0, 0

    def update(self):
        pass
    
    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(self.sx,self.sy)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.sx-8,self.sy-8,self.sx+8,self.sy+8
    
    def handle_collision(self,other,group):
        if group == "mario:fire_flowers":
            game_world.remove_object(self)

class LifeUpMushroom:
    def __init__(self, x = 0, y = 0):
        self.image = load_image("Resources/Items/1UP.png")
        self.x, self.y = x, y
        self.is_collision = False
        self.sx, self.sy = 0, 0

    def update(self):
        pass
    
    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(self.sx,self.sy)
        draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.sx-8,self.sy-8,self.sx+8,self.sy+8
    
    def handle_collision(self,other,group):
        if group == "mario:life_up_mushrooms":
            game_world.remove_object(self)

class Coin:
    def __init__(self, x = 0, y = 0):
        self.image = load_image("Resources/Items/coin.png")
        self.frame = 0
        self.x, self.y = 400, 50
        self.sprite_width, self.sprite_height = 16,16
        self.is_collision = False
        self.sx, self.sy = 0, 0

    def update(self):
        self.frame = (self.frame+1) % 4
        
    def draw(self):
        self.sx, self.sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.clip_draw(self.frame * self.sprite_width, 0, self.sprite_width, self.sprite_height, self.sx, self.sy)
        draw_rectangle(*self.get_bb())
        

    def get_bb(self):
        return self.sx-8,self.sy-8,self.sx+8,self.sy+8
    
    def handle_collision(self,other,group):
        if group == "mario:coins":
            game_world.remove_object(self)
    pass 