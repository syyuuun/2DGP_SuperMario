from pico2d import *
import game_world
import play_state
import server
from random import randint

MOVE_AMOUNT = 5

class Goomba:
    def __init__(self):
        self.image = load_image("Resources/Monsters/Goomba.png")
        self.x,self.y = randint(400,600), 58
        self.frame = 0
        self.face_dir = randint(-1,1)
        if 0== self.face_dir:
            self.face_dir = 1
        self.frame_bottom = 0
        self.temp_x = 0
        self.move_amount = MOVE_AMOUNT
        self.sprite_width = 47
        self.sprite_height = 61
        self.is_collision = False
        self.timer = 5
        self.is_die = False
        self.sx,self.sy = 0,0


    def update(self):
        self.frame = (self.frame+1) % 8
        if self.is_collision == False:
            self.x += self.face_dir * self.move_amount
            self.temp_x += MOVE_AMOUNT

        if self.temp_x > 100:
            self.temp_x  =0
            if self.face_dir == -1:
                self.face_dir = 1
            elif self.face_dir ==1:
                self.face_dir =-1

        if self.is_collision == True:
            self.timer -=1
            self.is_die = True
            print(self.timer)
        if self.timer < 0:
            self.x = -10
            self.y = -10
            game_world.remove_object(self)

    def draw(self):
        #self.sx,self.sy = self.x - play_s   
        if self.is_collision == True:
            self.frame_bottom = 164
            self.sprite_height = 54
            self.sprite_width = 63
            self.frame_bottom = 126
        else:
            if self.face_dir == -1:
                self.frame_bottom = 62
                pass
            elif self.face_dir == 1:
                self.frame_bottom = 0
                pass
        self.sx, self.sy = self.x - server.background.window_left, self.y-server.background.window_bottom
        self.image.clip_draw(
             self.frame * self.sprite_width, self.frame_bottom, self.sprite_width, self.sprite_height, self.sx, self.sy
        )
        
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.face_dir == -1:
            return self.sx - 20, self.sy -30, self.sx + 10, self.sy + 20
        elif self.face_dir == 1:
            return self.sx - 10, self.sy - 30, self.sx + 20, self.sy + 20
    
    def handle_collision(self,other,group):
        print("goomba die")        
        if group == "fire:goombas":
            self.is_collision = True

class Troopa:
    def __init__(self):
        self.image = load_image("Resources/Monsters/Troopa.png")
        self.x,self.y = randint(600,800), 58
        self.frame = 0
        self.face_dir = randint(-1,1)
        if 0== self.face_dir:
            self.face_dir = 1
        self.frame_bottom = 0
        self.temp_x = 0
        self.move_amount = MOVE_AMOUNT
        self.sprite_width  = 53
        self.sprite_height = 61 
        self.is_collision = False
        self.timer = 20
        self.is_die = False
        self.sx,self.sy = 0,0

    def update(self):
        self.frame = (self.frame+1) % 8
        if self.is_collision == False:
            self.x += self.face_dir * self.move_amount
            self.temp_x += MOVE_AMOUNT

        if self.temp_x > 100:
            self.temp_x = 0
            if self.face_dir == -1:
                self.face_dir = 1
            elif self.face_dir ==1:
                self.face_dir =-1

        if self.is_collision == True:
            self.is_die = True
            self.timer -=1
            print(self.timer)
        if self.timer < 0:
                self.x = -10
                self.y = -10
                game_world.remove_object(self)

    def draw(self):
        if self.is_collision == True:
            self.sprite_width = 32
            self.sprite_height = 30
            self.frame_bottom = 126
            self.y = 48
        else:
            if self.face_dir == -1:
                self.frame_bottom = 0
            elif self.face_dir == 1:
                self.frame_bottom = 61
        self.sx, self.sy = self.x - server.background.window_left, self.y-server.background.window_bottom
        self.image.clip_draw(
             self.frame * self.sprite_width, self.frame_bottom, self.sprite_width, self.sprite_height, self.sx, self.sy
        )
        
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        if self.face_dir == -1:
            return self.sx - 20, self.sy-30, self.sx + 10, self.sy + 20
        elif self.face_dir == 1:
            return self.sx -10, self.sy - 30, self.sx + 20, self.sy + 20 

    def handle_collision(self,other,group):
        print("troopa die")
        if group == "fire:troopas":
            self.is_collision = True

class Koopa:
    def __init__(self):
        self.image = load_image("Resources/Monsters/Koopa.png")
        self.x,self.y = randint(600,800), 58
        self.frame = 0
        self.sprite_width  = 90 
        self.sprite_height = 73 
        self.frame_bottom = 170
        self.is_collision = False
        self.attack_timer = 20
        self.is_die = False
        self.is_spawn = False 
        self.is_attacked = False
        self.hp = 1000 

        self.sx,self.sy = 0,0
    
    def update(self):
        self.frame = (self.frame+1) % 8
        
        # self.sprite_width  = 90 
        # self.sprite_height = 73 
        # self.frame_bottom = 170

        if True == self.is_die:
            self.sprite_width = 101
            self.sprite_height = 63
            self.frame_bottom = 243

        if True == self.is_attacked:
            self.sprite_width = 90
            self.sprite_height = 76
            self.frame_bottom = 0
            self.is_attacked = False 

        if  0 == self.hp:
            self.sprite_width = 102
            self.sprite_height = 74
            self.frame_bottom = 96 

        if self.hp < 0:
            self.is_die = True 
    
    def draw(self):

        self.sx, self.sy = self.x - server.background.window_left, self.y-server.background.window_bottom
        self.image.clip_draw(self.frame * self.sprite_width, self.frame_bottom, self.sprite_width, self.sprite_height, self.sx, self.sy)    
        
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.sx - 50, self.sy - 50, self.sx + 50, self.sy + 50 
        
    def handle_collision(self,other,group):
        if group == "fire:koopa":
            print("Koopa attaked by Mario's attack")
            self.hp -= 5
            self.is_attacked = True 
         
