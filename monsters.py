from pico2d import *
import game_world
from random import randint

MOVE_AMOUNT = 5

class Goomba:
    def __init__(self):
        self.image = load_image("Resources/Monsters/Goomba.png")
        self.x,self.y = randint(0,800), 58
        self.frame = 0
        self.face_dir = -1
        self.frame_bottom = 0
        self.temp_x = 0
        self.move_amount = MOVE_AMOUNT

    def update(self):
        self.x += self.face_dir * self.move_amount
        self.frame = (self.frame+1) % 8
        self.temp_x += MOVE_AMOUNT

        if self.temp_x > 100:
            self.temp_x  =0
            if self.face_dir == -1:
                self.face_dir = 1
            elif self.face_dir ==1:
                self.face_dir =-1

    def draw(self):
        if self.face_dir == -1:
            self.frame_bottom = 62
            pass
        elif self.face_dir == 1:
            self.frame_bottom = 0
            pass
        
        self.image.clip_draw(
             self.frame * 47, self.frame_bottom, 47, 61, self.x, self.y
        )
        
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.face_dir == -1:
            return self.x - 20, self.y -30, self.x + 10, self.y + 20
        elif self.face_dir == 1:
            return self.x - 10, self.y - 30, self.x + 20, self.y + 20
    
    def handle_collision(self,other,group):
        print("goomba die")        
        if group == "mario:goombas":
            game_world.remove_object(self)

class Troopa:
    def __init__(self):
        self.image = load_image("Resources/Monsters/Troopa.png")
        self.x,self.y = randint(0,800), 58
        self.frame = 0
        self.face_dir = -1
        self.frame_bottom = 0
        self.temp_x = 0
        self.move_amount = MOVE_AMOUNT

    def update(self):
        self.x += self.face_dir * self.move_amount
        self.frame = (self.frame+1) % 8
        self.temp_x += MOVE_AMOUNT

        if self.temp_x > 100:
            self.temp_x  =0
            if self.face_dir == -1:
                self.face_dir = 1
            elif self.face_dir ==1:
                self.face_dir =-1

    def draw(self):
        if self.face_dir == -1:
            self.frame_bottom = 0
            pass
        elif self.face_dir == 1:
            self.frame_bottom = 61
            pass
        
        self.image.clip_draw(
             self.frame * 53, self.frame_bottom, 53, 61, self.x, self.y
        )
        
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.face_dir == -1:
            return self.x - 20, self.y-30, self.x + 10, self.y + 20
        elif self.face_dir == 1:
            return self.x -10, self.y - 30, self.x + 20, self.y + 20 

    def handle_collision(self,other,group):
        print("troopa die")
    
        if group == "mario:troopas":
            game_world.remove_object(self)