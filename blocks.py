from pico2d import *
from random import randint
import game_world
from items import FireFlower
from items import Mushroom
from items import LifeUpMushroom
from items import Coin
#import play_state
import server

flower = None
coin = None
mushroom = None
life_mushroom = None

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
        #draw_rectangle(*self.get_bb())
    
    def update(self):
        pass

    def get_bb(self):
        return self.sx - 8, self.sy - 8, self.sx + 8, self.sy + 8

    def handle_collision(self,other,group):
        print("collision")
        global flower, mushroom,life_mushroom, coin
        x,y = self.x, self.y +10
      
        if "mario:item_blocks" == group:
            random = randint(0,3)
            if 0 == random:
                flower = FireFlower(x,y)
                game_world.add_object(flower,1)
                game_world.add_collision_group(server.mario,flower,"mario:fire_flowers")
                game_world.remove_object(self)
            elif 1 == random:
                coin = Coin(x,y)
                game_world.add_object(coin,1)
                game_world.add_collision_group(server.mario,coin,"mario:coins")
                game_world.remove_object(self)
            elif 2 == random:
                mushroom = Mushroom(x,y)
                game_world.add_object(mushroom,1)
                game_world.add_collision_group(server.mario,mushroom,"mario:mushrooms")
                game_world.remove_object(self)
            
            elif 3 == random:
                life_mushroom  = LifeUpMushroom(x,y)
                game_world.add_object(life_mushroom,1)
                game_world.add_collision_group(server.mario,life_mushroom,"mario:life_up_mushrooms")
                game_world.remove_object(self)

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
        #draw_rectangle(*self.get_bb())
    
    def update(self):
        pass

    def get_bb(self):
        return self.sx - 8, self.sy - 8, self.sx + 8, self.sy + 8

    def handle_collision(self,other,group):
        pass