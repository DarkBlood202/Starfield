import pygame as pg
import random
from settings import *
from methods import *

class Star:
    def __init__(self):
        self.x = random.randint(-WIDTH,WIDTH)
        self.y = random.randint(-HEIGHT,HEIGHT)
        self.z = random.randint(0,WIDTH)

        self.pz = self.z

    def update(self):
        self.z -= STAR_SPEED
        if self.z < 1:
            self.z = WIDTH
            self.x = random.randint(-WIDTH, WIDTH)
            self.y = random.randint(-HEIGHT, HEIGHT)
            self.pz = self.z

    def show(self,screen):

        sx = int(remap(self.x/self.z,0,1,0,WIDTH))
        sy = int(remap(self.y/self.z,0,1,0,HEIGHT))

        r = int(remap(self.z,0,WIDTH,8,0))

        pg.draw.circle(screen,C_WHITE,(sx+WIDTH//2,sy+HEIGHT//2),r)

        px = int(remap(self.x/self.pz,0,1,0,WIDTH))
        py = int(remap(self.y/self.pz,0,1,0,HEIGHT))

        self.pz = self.z
        pg.draw.line(screen,C_WHITE,(px+WIDTH//2,py+HEIGHT//2),(sx+WIDTH//2,sy+HEIGHT//2))