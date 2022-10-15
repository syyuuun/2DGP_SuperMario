from pico2d import *
import game_framework
import play_state
import title_state

pico2d.open_canvas()
game_framework.run(title_state)
pico2d.close_canvas()