from pico2d import *

VELOCITY = 6
MASS = 2

#이벤트 정의
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SPACE, TIMER = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT) : LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT) : RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}
class IDLE:
    @staticmethod
    def enter(self,event):
        self.dir = 0
        print("ENTER IDLE")
    @staticmethod
    def exit(self):
        print("EXIT IDLE")

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
        if event == RIGHT_DOWN: self.dir+=1
        elif event == LEFT_DOWN: self.dir -=1
        elif event == RIGHT_UP: self.dir-=1
        elif event == LEFT_UP: self.dir +=1
    def exit(self):
        print("EXIT RUN")
        self.face_dir = self.dir
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir*5
        if self.dir == -1:
            self.frame_bottom = 80
        elif self.dir == 1:
            self.frame_bottom = 120
    def draw(self):
        self.image.clip_draw(
             self.frame * 40, self.frame_bottom, 40, 40, self.x, self.y)
class JUMP:
    def enter(self,event):
        print("ENTER JUMP")
    def exit(self):
        print("EXIT JUMP")
    def do(self):
        self.frame = (self.frame + 1) % 8

        if self.velocity > 0:
            F = (0.5 * self.mass * (self.velocity * self.velocity))
        else:
            F = -(0.5 * self.mass * (self.velocity * self.velocity))

        self.y += round(F)

        self.velocity -= 1

        if self.y < 50:
            self.y = 50
            self.velocity = VELOCITY
            self.add_event(TIMER)

        self.x += self.dir * 5

        if self.face_dir == -1:
            self.frame_bottom = 0

        elif self.face_dir == 1:
            self.frame_bottom = 40
    def draw(self):
        self.image.clip_draw(
            self.frame * 40, self.frame_bottom, 40, 40, self.x, self.y)

next_state = {
    IDLE:{RIGHT_DOWN : RUN, LEFT_DOWN: RUN, RIGHT_UP: IDLE, LEFT_UP: IDLE, SPACE: JUMP},
    RUN:{RIGHT_DOWN: IDLE, LEFT_DOWN: IDLE, RIGHT_UP: IDLE, LEFT_UP: IDLE, SPACE: JUMP},
    JUMP:{RIGHT_DOWN: RUN, LEFT_DOWN: RUN, RIGHT_UP: IDLE, LEFT_UP: IDLE,SPACE: JUMP, TIMER:IDLE }
}

class Mario:
    def add_event(self,event):
        self.q.insert(0,event)
    def handle_event(self,event):
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            self.add_event(key_event)

    def __init__(self):
        self.image = load_image("Resources/Mario/mario_animation_all.png")
        self.x, self.y = 200, 50
        self.frame = 0
        self.dir,self.face_dir = 0,1
        self.q = []
        self.frame_bottom = 0
        self.is_jump =0
        self.velocity = VELOCITY
        self.mass = MASS
        self.cur_state = IDLE
        self.cur_state.enter(self,None)

    def update(self):
        self.cur_state.do(self)

        if self.q:
            event = self.q.pop()  # 이벤트를 가져오고
            self.cur_state.exit(self)  # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event]  # 다음 상태를 계산
            self.cur_state.enter(self, event) # 진입

        # if self.is_jump > 0:
        #
        #     if self.is_jump == 2:
        #         self.velocity = VELOCITY
        #
        #     if self.velocity > 0:
        #         F = (0.5 * self.mass * (self.velocity * self.velocity))
        #     else:
        #         F = -(0.5 * self.mass * (self.velocity * self.velocity))
        #
        #     self.y += round(F)
        #
        #     self.velocity -= 1
        #
        #     if self.y < 50:
        #         self.y = 50
        #         self.is_jump = 0
        #         self.velocity = VELOCITY
        #
        # self.x += self.dir * 5
        # self.frame = (self.frame+1) % 8

    # def jump(self,j):
    #     self.is_jump = j

    def draw(self):
        self.cur_state.draw(self)

