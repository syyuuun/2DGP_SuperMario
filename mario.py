from pico2d import *
from fire import Fire
import game_world

VELOCITY = 6
MASS = 2

#1: EVENT
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, A, SPACE = range(6)

event_name = {"RIGHT_DOWN","LEFT_DOWWN", "RIGHT_UP", "LEFT_UP","A", "SPACE" }

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
        self.frame = (self.frame + 1) % 8
    
    def draw(self):
        if self.face_dir == 1:
            self.frame_bottom = 200
        elif self.face_dir == -1:
            self.frame_bottom = 160
        self.image.clip_draw(
            self.frame * 40, self.frame_bottom, 40, 40, self.x, self.y)

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
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.dir == -1:
            self.frame_bottom = 80
        elif self.dir == 1:
            self.frame_bottom = 120
 
    def draw(self):
        self.image.clip_draw(
             self.frame * 40, self.frame_bottom, 40, 40, self.x, self.y)

# STATE CHANGE
next_state = {
    IDLE:{RIGHT_DOWN : RUN, LEFT_DOWN: RUN, RIGHT_UP: IDLE, LEFT_UP: IDLE, A: IDLE, SPACE: IDLE },
    RUN:{RIGHT_DOWN: IDLE, LEFT_DOWN: IDLE, RIGHT_UP: IDLE, LEFT_UP: IDLE, A:RUN, SPACE: RUN}
}

class Mario:
    def __init__(self):
        self.image = load_image("Resources/Mario/mario_animation_all.png")
        self.x, self.y = 200, 50
        self.frame = 0
        self.dir,self.face_dir = 0,1
        self.event_queue = []
        self.frame_bottom = 0
        self.is_jump = False
        self.velocity = VELOCITY
        self.mass = MASS
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

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

        # if self.is_jump > 0:
        
        #     if self.is_jump == 2:
        #         self.velocity = VELOCITY

        if True == self.is_jump:
            if self.velocity > 0:
                F = (0.5 * self.mass * (self.velocity * self.velocity))
            else:
                F = -(0.5 * self.mass * (self.velocity * self.velocity))
        
            self.y += round(F)
        
            self.velocity -= 1
            
            if self.y < 50:
                self.y = 50
                self.is_jump = False
                self.velocity = VELOCITY
            
            self.x += self.dir * 5
            self.frame = (self.frame+1) % 8

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self,event):
        self.event_queue.insert(0,event)
        
    def handle_event(self,event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)

    def attack(self):
        print("ATTACK")
        fire = Fire(self.x,self.y,self.face_dir*10)
        game_world.add_object(fire,1)
        
    def jump(self):
        self.is_jump = True 
