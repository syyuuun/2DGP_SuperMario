from pico2d import *
import game_framework
import game_world
import title_state

from mario import Mario
from world import World

world = None
mario = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            mario.handle_event(event)

def enter():
    global world, mario
    world = World()
    mario = Mario()
    game_world.add_object(world,0)
    game_world.add_object(mario,1)

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()

def draw_wolrd():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_wolrd()
    delay(0.05)
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()