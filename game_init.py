import pygame as pg
import sys
from entities import *
from settings import *

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.clock = pg.time.Clock()

    def new_game(self):
        self.stars = []
        for i in range(NUMBER_OF_STARS):
            self.stars.append(Star())

    def run(self):
        self.running = True
        while self.running:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill(C_BACKGROUND)

        for i in range(NUMBER_OF_STARS):
            self.stars[i].update()
            self.stars[i].show(self.screen)

        pg.display.flip()

    def events(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                self.quit()

if __name__ == "__main__":
    g = Game()
    while True:
        g.new_game()
        g.run()