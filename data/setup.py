import pygame as pg
from . import constants as c
from . import tools
import os

pg.init()
pg.display.set_caption(c.CAPTION)
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

GFX = tools.load_all_gfx(os.path.join('resources', 'graphics'))
FONTS = tools.load_all_fonts(os.path.join('resources', 'fonts'))
