from pico2d import *

import server

class BackGround:
    def __init__(self):
        self.image = load_image("Resources/Map/test_map.png")
        self.canvas_width =  get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left,self.window_bottom,self.canvas_width+40,self.canvas_height,0,0)

    def update(self):
        self.window_left = clamp(0, int(server.mario.x) - self.canvas_width//8, self.w - self.canvas_width - 1)
        self.window_bottom = clamp(0, int(server.mario.y) - self.canvas_height//2, self.h - self.canvas_height - 1)
        
    def handle_event(self, event):
        pass
