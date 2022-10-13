#from typing_extensions import clear_overloads
from pico2d import *
import game_framework
import title_state

class World:
    def __init__(self):
        self.image = load_image("Resources/Map/World1-1.png")

    def draw(self):
       self.image.draw(3280//2,232//2)

class BackGround:
    def __init__(self):
        self.image = load_image("Resources/Map/back_ground.png")

    def draw(self):
        self.image.draw(0,600,3280,1200)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)

back_ground = None
world = None

def enter():
    global back_ground,world
    back_ground = BackGround()
    world = World()

def update():
    pass

def draw_back_ground():
    back_ground.draw()

def draw_wolrd():
    world.draw()

def draw():
    clear_canvas()
    draw_back_ground()
    draw_wolrd()
    delay(0.05)
    update_canvas()

def pause():
    pass

def resume():
    pass

def exit():
    global back_ground,world
    del back_ground
    del world

