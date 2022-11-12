from pickletools import read_unicodestringnl
from pico2d import *
from mario import Mario 
import csv 

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

class World:
    def __init__(self):
        #self.image = load_image("Resources/Map/World1-1.png")


        self.data = list()
        f = open("Resources/Map/map_tile.csv",'r')
        reader = csv.reader(f)

        for row in reader:
            self.data.append(row)
        f.close

        for data in self.data:
            print(data)

        self.image = load_image("Resources/Map/map.png")
        self.x = 3840 // 2
        self.y =  640 // 2
        self.offset_x = 0
        self.offset_y = 0
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.w = 3840
        self.h = 640 

    def update(self):
        self.offset_x -=1
        pass 

    def draw(self):
       self.image.draw(self.x +self.offset_x,self.y+self.offset_y)
