from pico2d import *
import game_framework
import title_state
from  mario import Mario 
from world import World
from background import BackGround

back_ground = None
world = None
mario = None

def handle_events():
    global mario
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                mario.dir -= 1
                mario.frame_bottom = 80
                pass
            elif event.key == SDLK_RIGHT:
                mario.dir += 1
                mario.frame_bottom = 120
                pass
            elif event.key == SDLK_SPACE:
                if mario.is_jump == 0:
                    mario.jump(1)
                elif mario.is_jump ==1 :
                    mario.jump(2)
                pass
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                mario.dir += 1
                mario.frame_bottom = 160
                pass
            elif event.key == SDLK_RIGHT:
                mario.dir -= 1
                mario.frame_bottom = 200
                pass


def enter():
    global back_ground, world, mario
    back_ground = BackGround()
    world = World()
    mario = Mario()


def update():
    mario.update()
    pass


def draw_back_ground():
    back_ground.draw()


def draw_wolrd():
    world.draw()


def draw_mario():
    mario.draw()


def draw():
    clear_canvas()
    draw_back_ground()
    draw_wolrd()
    draw_mario()
    delay(0.05)
    update_canvas()


def pause():
    pass


def resume():
    pass


def exit():
    global back_ground, world, mario
    del back_ground
    del world
    del mario
