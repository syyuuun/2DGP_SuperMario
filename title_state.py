from pico2d import *
import game_framework
import play_state

image = None 
bgm = None

def enter():
    global image,bgm 
    image = load_image("Resources/Scene/title.png")
    bgm = load_music("Resources/Sound/Super Mario Bross - Theme Song.mp3")
    bgm.set_volume(20)
    bgm.play()
    
def exit():
    global image,font
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(play_state)

def draw():
    global image,font
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass