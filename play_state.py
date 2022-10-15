from pico2d import *
import game_framework
import title_state


class World:
    def __init__(self):
        self.image = load_image("Resources/Map/World1-1.png")

    def draw(self):
       self.image.draw(3280//2, 232//2)


class BackGround:
    def __init__(self):
        self.image = load_image("Resources/Map/back_ground.png")

    def draw(self):
        self.image.draw(0, 600, 3280, 1200)


class Mario:
    def __init__(self):
        self.image = load_image("Resources/Mario/mario_animation_all.png")
        self.x, self.y = 400, 50
        self.frame = 0
        self.dir = 0
        self.frame_bottom = 0

    def update(self):
        self.x += self.dir * 5
        self.frame = (self.frame+1) % 8

    def draw(self):
        self.image.clip_draw(
            self.frame * 40, self.frame_bottom, 40, 40, self.x, self.y)


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
            elif event.key == SDLK_UP:
                pass
            elif event.key == SDLK_DOWN:
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


back_ground = None
world = None
mario = None


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
