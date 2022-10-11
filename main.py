from pico2d import *

class World:
    def __init__(self):
        self.image = load_image("Resources/Map/World1-1.png")

    def render(self):
       self.image.draw(3280//2,232//2)

class BackGround:
    def __init__(self):
        self.image = load_image("Resources/Map/back_ground.png")

    def render(self):
        self.image.draw(0,600,3280,1200)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            ruuning = False

open_canvas()

back_ground = BackGround()
world = World()
running = True

# Game main loop  
while running:
    #Input Process 
    handle_events()

    #Game logic - update

    #Rendering
    back_ground.render()
    world.render()
    delay(0.05)
    update_canvas()

close_canvas()
