from pico2d import *
import game_world
from random import randint

MOVE_AMOUNT = 5

class Goomba:
    def __init__(self):
        self.image = load_image("Resources/Monsters/Goomba.png")
        self.x,self.y = 600, 40
        self.frame = 0
        self.face_dir = -1
        self.frame_bottom = 0
        self.temp_x = 0
        self.rect_left = self.x - 20
        self.rect_top = self.y + 20
        self.rect_right = self.x + 10
        self.rect_bottom = self.y - 30
        self.move_amount = MOVE_AMOUNT

    def update(self):
        self.x += self.face_dir * self.move_amount
        self.frame = (self.frame+1) % 8
        self.temp_x += MOVE_AMOUNT
        self.rect_left = self.x - 20
        self.rect_top = self.y + 20
        self.rect_right = self.x + 10
        self.rect_bottom = self.y - 30

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
        
        draw_rectangle(self.rect_left,self.rect_top,self.rect_right,self.rect_bottom)