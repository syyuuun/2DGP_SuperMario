from pico2d import *
from random import randint
import game_world

class ItemBlocks:
    def __init__(self, x = 0, y = 0):
        self.image = load_image("Resources/Blocks/item_block.png")
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.width,self.height = 16,16
        self.x,self.y = randint(0,800),100
        self.is_collision = False
        pass
    
    def draw(self):
        self.image.draw(self.x,self.y,16,16)
        draw_rectangle(*self.get_bb())
    
    def update(self):
        pass

    def get_bb(self):
        return self.x - 8, self.y - 8, self.x + 8, self.y + 8

    def handle_collision(self,other,group):
        pass




class FloorBrick:
    def __init__(self, x = 0, y = 0):
        self.image = load_image("Resources/Blocks/brick.png")
        self.x,self.y = x,y
        self.is_collision = False
        self.width,self.height = 16,16
        pass
    
    def draw(self):
        self.image.draw(self.x,self.y,self.width,self.height)
        draw_rectangle(*self.get_bb())
    
    def update(self):
        pass

    def get_bb(self):
        return self.x - 8, self.y - 8, self.x + 8, self.y + 8

    def handle_collision(self,other,group):
        pass