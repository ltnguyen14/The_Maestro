import pygame as pg
from .. import tools, setup
from .. import constants as c

class Menu(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.test_image = setup.GFX['rect_box']

    def update(self, screen, keys):
        screen.fill(c.RED)
        screen.blit(self.test_image, (0,0))
        pass
