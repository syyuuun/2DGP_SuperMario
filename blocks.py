from pico2d import *
from random import randint
import game_world
#import play_state
import server

class ItemBlocks:
    def __init__(self, x = 0, y = 0):
        self.image = load_image("Resources/Blocks/item_block.png")
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.width,self.height = 16,16
        self.x,self.y = randint(0,server.background.w),100
        self.is_collision = False
        self.sx,self.sy = 0,0
        pass
    
    def draw(self):
        self.sx,self.sy = self.x - server.background.window_left,self.y-server.background.window_bottom
        self.image.draw(self.sx,self.sy)
        draw_rectangle(*self.get_bb())
    
    def update(self):
        pass

    def get_bb(self):
        return self.sx - 8, self.sy - 8, self.sx + 8, self.sy + 8

    def handle_collision(self,other,group):
        pass

class FloorBrick:
    def __init__(self, x = 0, y = 0):
        self.image = load_image("Resources/Blocks/brick.png")
        self.x,self.y = x,y
        self.is_collision = False
        self.width,self.height = 16,16
        self.sx = 0
        self.sy = 0
        pass
    
    def draw(self):
        self.sx,self.sy = self.x - server.background.window_left,self.y - server.background.window_bottom
        self.image.draw(self.sx,self.sy)
        draw_rectangle(*self.get_bb())
    
    def update(self):
        pass

    def get_bb(self):
        return self.sx - 8, self.sy - 8, self.sx + 8, self.sy + 8

    def handle_collision(self,other,group):
        pass