import pygame as pg
from .. import setup, tools
from .. import constants as c

class text_box(object):
    def __init__(self, size, text, text_color, position, normal_box, center=False, text_size=30):
        self.text = text
        self.text_color = text_color
        self.surface = pg.display.get_surface()

        self.normal_image = setup.GFX[normal_box]
        self.normal_image = pg.transform.smoothscale(self.normal_image, size)

        self.rect = self.normal_image.get_rect()
        if not center:
            self.rect.x, self.rect.y = position[0], position[1]
        else:
            self.rect.center = position

        self.normal_font = pg.font.Font(setup.FONTS['Aller_Rg'], text_size)

    def blit_text(self):
        tools.drawText(self.surface, self.text, self.text_color, self.rect, self.normal_font)

    def update(self, mouse_state, mouse_pos):
        self.draw()
        if mouse_state[0]:
            return self.text

    def draw(self):
        self.surface.blit(self.normal_image, self.rect)
        self.blit_text()
