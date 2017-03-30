import pygame as pg
from .. import tools, setup

class Menu(object):
    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def update(self, screen, keys):
        pass
