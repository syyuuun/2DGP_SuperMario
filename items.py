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
        if group == "mario:stars":
            game_world.remove_object(self)