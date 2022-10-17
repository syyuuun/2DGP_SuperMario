from pico2d import *
import game_framework
import title_state
VELOCITY = 6
MASS = 2 

class Mario:
    def __init__(self):
        self.image = load_image("Resources/Mario/mario_animation_all.png")
        self.x, self.y = 400, 50
        self.frame = 0
        self.dir = 0
        self.frame_bottom = 0
        self.is_jump =0
   
        self.velocity = VELOCITY
        self.mass = MASS   

    def update(self):
        if self.is_jump > 0:
            if self.is_jump == 2:
                self.velocity = VELOCITY

            if self.velocity > 0:
                F = (0.5 * self.mass * (self.velocity * self.velocity))
            else:
                F = -(0.5 * self.mass * (self.velocity * self.velocity))
            
            self.y += round(F)

            self.velocity -= 1 

            if self.y < 50:
                self.y = 50
                self.is_jump = 0
                self.velocity = VELOCITY
            
        self.x += self.dir * 5
        self.frame = (self.frame+1) % 8

    def jump(self,j):
        self.is_jump = j

    def draw(self):
        self.image.clip_draw(
            self.frame * 40, self.frame_bottom, 40, 40, self.x, self.y)



