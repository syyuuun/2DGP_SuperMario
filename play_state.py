from pico2d import *
import game_framework
import game_world
import title_state

from mario import Mario
from world import World
from monsters import Goomba 
from monsters import Troopa

world = None
mario = None
goombas = None
troopas = None 
fire = None

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
    global world, mario, goombas, troopas,fire
    world = World()
    mario = Mario()
    goombas = [Goomba() for i in range(5)]
    troopas = [Troopa() for i in range(5)]
    game_world.add_object(world,0)
    game_world.add_object(mario,1)
    game_world.add_objects(goombas,1)
    game_world.add_objects(troopas,1)

    game_world.add_collision_group(mario,troopas,"mario:troopas")
    game_world.add_collision_group(mario,goombas,"mario:goombas")
    game_world.add_collision_group(fire,troopas, "fire:troopas")
    game_world.add_collision_group(fire,goombas, "fire:goombas")





    

def exit():
    game_world.clear()

def update():
    for game_object in game_world.all_objects():
        game_object.update()
    
    for a,b,group in game_world.all_collision_pairs():
        if check_collision(a,b):
            print("COLLISION by",group)
            a.handle_collision(b,group)
            b.handle_collision(a,group)
    
    delay(0.05)
        
def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass


def check_collision(a,b):
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb:
        return False
    if ra < lb:
        return False
    if ta < bb:
        return False
    if ba > tb:
        return False

    return True

def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()