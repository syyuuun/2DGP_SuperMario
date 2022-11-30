from pico2d import *
from fire import Fire
from monsters import Goomba
from monsters import Troopa
from items import FireFlower
from items import Mushroom
from items import LifeUpMushroom
import play_state 
import game_framework
import game_world
import title_state
import game_over_state

import server

VELOCITY = 6
MASS = 2
MOVE_AMOUNT = 7 

#1: EVENT
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, A, SPACE, LIFE, TIMER = range(8)

event_name = {"RIGHT_DOWN","LEFT_DOWWN", "RIGHT_UP", "LEFT_UP","A", "SPACE"}

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT) : LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT) : RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_a): A,
    (SDL_KEYDOWN, SDLK_SPACE) : SPACE 
}

#2: STATE
class IDLE:
    @staticmethod
    def enter(self,event):
        self.dir = 0
        print("ENTER IDLE")
    
    @staticmethod
    def exit(self,event):
        print("EXIT IDLE")
        if A == event:
            self.attack()
        if SPACE == event:
            self.jump()

    @staticmethod
    def do(self):
        if self.num_of_mario_life <=0:
            self.add_event(LIFE)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8 
    def draw(self):
        if self.size == "SMALL":
            self.sprite_width = 40
            self.sprite_height = 25
            if self.is_jump:
                if -1 == self.face_dir:
                    self.frame_bottom = 25
                elif 1 == self.face_dir:
                    self.frame_bottom = 50
            else:
                if self.face_dir == 1:
                    self.frame_bottom = 150
                elif self.face_dir == -1:
                    self.frame_bottom = 125
            
            sx,sy = self.x - server.background.window_left , self.y -server.background.window_bottom
            self.small_mario_image.clip_draw(
            int(self.frame) * self.sprite_width, self.frame_bottom, self.sprite_width, self.sprite_height, sx, sy)
        elif self.size == "MEDIUM":
            self.sprite_width = 40
            self.sprite_height = 40
            if self.is_jump:
                if -1 == self.face_dir:
                    self.frame_bottom = 40
                elif 1 == self.face_dir:
                    self.frame_bottom = 80
            else:
                if self.face_dir == 1:
                    self.frame_bottom = 240
                elif self.face_dir == -1:
                    self.frame_bottom = 200
            sx,sy = self.x - server.background.window_left , self.y -server.background.window_bottom
            self.image.clip_draw(
            int(self.frame) * self.sprite_width, self.frame_bottom, self.sprite_width, self.sprite_height, sx, sy)

class RUN:
    def enter(self, event):
        print("ENTER RUN")
        if event == RIGHT_DOWN:
            self.dir+=1
        elif event == LEFT_DOWN: 
            self.dir -=1
        elif event == RIGHT_UP: 
            self.dir-=1
        elif event == LEFT_UP: 
            self.dir +=1
 
    def exit(self,event):
        print("EXIT RUN")
        self.face_dir = self.dir
        if A == event:
            self.attack()
        if SPACE == event:
            self.jump()

    def do(self):
        if self.num_of_mario_life <=0:
            self.add_event(LIFE)
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8 
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        
        if "SMALL" == self.size:
            self.x = clamp(0 + 15, self.x, server.background.w - 1 - 15)
            self.y = clamp(0 + 15, self.y, server.background.h - 1 - 15)
        
        elif "MEDIUM" == self.size:
            self.x = clamp(0 + 15, self.x, server.background.w - 1 - 15)
            self.y = clamp(0 + 20, self.y, server.world.h - 1 - 20)
        
        if self.size == "SMALL":
            if self.dir == -1:
                self.frame_bottom = 75
            elif self.dir == 1:
                self.frame_bottom = 100
            pass
        elif self.size == "MEDIUM":
            if self.dir == -1:
                self.frame_bottom = 120
            elif self.dir == 1:
                self.frame_bottom = 160

    def draw(self):
        #self.x,self.y - self.x  - play_state.world.window_left, self.y - play_state.world.window_bottom
        sx,sy = self.x - server.background.window_left , self.y -server.background.window_bottom
        if self.size == "SMALL":
            self.small_mario_image.clip_draw(
             int(self.frame) * self.sprite_width, self.frame_bottom,self.sprite_width, self.sprite_height, sx, sy)
            pass
        elif self.size == "MEDIUM":
            self.image.clip_draw(
             int(self.frame) * 40, self.frame_bottom, 40, 40, sx, sy)

class DIE:
    def enter(self,event):
        pass

    def exit(self,event):
        pass

    def do(self):
        self.die_timer -=1
        self.frame_bottom = 0
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.y -= 5
        if self.die_timer <=0:
            game_framework.change_state(game_over_state)
    def draw(self):
        sx,sy = self.x - server.background.window_left , self.y -server.background.window_bottom
        self.small_mario_image.clip_draw(
        int(self.frame) * self.sprite_width, self.frame_bottom,self.sprite_width, self.sprite_height, sx, sy)

# STATE CHANGE
next_state = {
    IDLE:{RIGHT_DOWN : RUN, LEFT_DOWN: RUN, RIGHT_UP: IDLE, LEFT_UP: IDLE, A: IDLE, SPACE: IDLE, LIFE: DIE },
    RUN:{RIGHT_DOWN: IDLE, LEFT_DOWN: IDLE, RIGHT_UP: IDLE, LEFT_UP: IDLE, A:RUN, SPACE: RUN, LIFE: DIE},
    DIE:{RIGHT_DOWN : DIE, LEFT_DOWN: DIE, RIGHT_UP: DIE, LEFT_UP: DIE, A: DIE, SPACE: DIE}
}

PIXEL_PER_METER = 10.0 / 0.3
RUN_SPEED_KPH = 5.0
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

FONT_SIZE = 25
fire = None

class Mario:
    def __init__(self):
        # attribute
        self.is_jump = False
        self.velocity = VELOCITY
        self.mass = MASS
        self.move_amount = MOVE_AMOUNT
        self.num_of_mario_life =4
        self.die_timer = 20
        self.size = "SMALL"
        self.is_get_fire_flowers = False
        self.is_collision_item_block = False

        # image and font 
        self.image = load_image("Resources/Mario/mario_sprites.png")
        self.small_mario_image = load_image("Resources/Mario/small_mario_sprites.png")
        self.mario_heart_image = load_image("Resources/Mario/mario_heart.png")
        self.font = load_font("Resources/Font/ENCR10B.TTF",FONT_SIZE)
        
        # position
        self.x, self.y = 200, 44
        self.frame = 0
        self.dir,self.face_dir = 0,1
        self.sprite_width = 40
        self.sprite_height = 25
        self.frame_bottom = 0

        # event
        self.event_queue = []

        # state
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

        # sound 
        self.fire_sound = load_wav("Resources/Sound/fire.wav")
        self.fire_sound.set_volume(15)
        self.jump_sound = load_wav("Resources/Sound/jump.wav")
        self.jump_sound.set_volume(15)
        self.power_down = load_wav("Resources/Sound/smb_pipe.wav")
        self.power_down.set_volume(15)
        self.power_up = load_wav("Resources/Sound/smb_powerup.wav")
        self.power_up.set_volume(15)
        self.life_up = load_wav("Resources/Sound/smb_1-up.wav")
        self.life_up.set_volume(15)

    def update(self):
        self.cur_state.do(self)

        if self.event_queue:
            event = self.event_queue.pop()  # 이벤트를 가져오고
            self.cur_state.exit(self,event)  # 현재 상태를 나가고
            try:
                self.cur_state = next_state[self.cur_state][event]  # 다음 상태를 계산
            except KeyError:
                print("ERROR: ",self.cur_state.__name__, " ", event_name[event])
        
            self.cur_state.enter(self, event) # 진입
        
        # JUMP
        if True == self.is_jump:
            if self.velocity > 0:
                F = (0.5 * self.mass * (self.velocity * self.velocity))
            else:
                F = -(0.5 * self.mass * (self.velocity * self.velocity))

            self.y += round(F)

            self.velocity -= 1

            if self.y < 50:
                self.y = 45
                self.is_jump = False
                self.velocity = VELOCITY

            
            if self.size == "SMALL":
                if -1 == self.face_dir:
                    self.frame_bottom = 25
                elif 1 == self.face_dir:
                    self.frame_bottom = 50
            elif self.size == "MEDIUM":
                if -1 == self.face_dir:
                    self.frame_bottom = 40
                elif 1 == self.face_dir:
                    self.frame_bottom = 80

        if self.num_of_mario_life <= 0:
            pass

        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8 
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
       # print(f"X:{self.x},Y:{self.y}")
    def draw(self): 
        self.cur_state.draw(self)
        self.font.draw(0,get_canvas_height()-20,"MARIO LIFE: ",(0,0,0))

        draw_rectangle(*self.get_bb())

        for i in range(self.num_of_mario_life):
           self.mario_heart_image.draw(180 + (i*30),get_canvas_height()-20,20,20)

    def add_event(self,event):
        self.event_queue.insert(0,event)
        
    def handle_event(self,event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)

    def attack(self): 
        if True == self.is_get_fire_flowers:
            global fire
            print("ATTACK")
            self.fire_sound.play()
            fire = Fire(self.x,self.y,self.face_dir*20)
            game_world.add_object(fire,1)
            game_world.add_collision_group(fire, server.troopas, "fire:troopas")
            game_world.add_collision_group(fire, server.goombas, "fire:goombas")
            game_world.add_collision_group(fire, server.koopa, "fire:koopa")

    def jump(self):
        print("JUMP")
        self.is_jump = True 
        self.jump_sound.play()

    def get_bb(self):
        sx,sy = self.x - server.background.window_left , self.y -server.background.window_bottom
        if self.size == "SMALL":
            return sx-12, sy - 13, sx + 10, sy + 8
        elif self.size == "MEDIUM":
            return sx-15, sy - 20, sx + 15, sy + 20 

    def handle_collision(self,other,group):
        print(group)
        if group == "mario:mushrooms":
            if self.size == "SMALL":
                self.size = "MEDIUM"
            self.power_up.play()
            
        elif group == "mario:fire_flowers":
            if self.size == "SMALL":
                self.size = "MEDIUM"
            self.is_get_fire_flowers = True
            self.power_up.play()
            
        elif group == "mario:stars":
            if self.num_of_mario_life < 5:
                self.num_of_mario_life +=1
            self.life_up.play()

        elif group == "mario:item_blocks":
            #print("COLLISIOn mario and item_block")
            global flower
            flower = FireFlower(other.x,other.y)
            game_world.add_object(flower,1)
            game_world.add_collision_group(server.mario, flower, "mario:fire_flowers")
            pass

        elif group == "mario:floor_bricks":
            pass

        if False == other.is_collision:
            if group == "mario:troopas" or group == "mario:goombas" or group=="mario:koopa":
                if self.size == "SMALL":
                    self.num_of_mario_life -=1
                elif self.size == "MEDIUM":
                    self.size = "SMALL"
                    self.is_get_fire_flowers = False
                self.power_down.play()