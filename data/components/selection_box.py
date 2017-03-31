import pygame as pg
from .. import setup
from .. import constants as c

class selection_box(object):
    def __init__(self, size, text, text_color, position, normal_box, hl_box, center=False, text_size=30):
        self.text = text
        self.highlight = False
        self.surface = pg.display.get_surface()

        self.hl_image = setup.GFX[hl_box]
        self.normal_image = setup.GFX[normal_box]

        self.hl_image = pg.transform.smoothscale(self.hl_image, size)
        self.normal_image = pg.transform.smoothscale(self.normal_image, size)

        self.rect = self.normal_image.get_rect()
        if not center:
            self.rect.x, self.rect.y = position[0], position[1]
        else:
            self.rect.center = position

        self.normal_font = pg.font.Font(setup.FONTS['Aller_Rg'], text_size)
        self.label = self.normal_font.render(self.text, 1, text_color)
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.center

    def blit_text(self):
        self.surface.blit(self.label, self.label_rect)

    def update(self, mouse_state, mouse_pos):
        self.draw()
        if mouse_state[0]:
            return self.text

    def draw(self):
        if self.highlight:
            self.surface.blit(self.hl_image, self.rect)
            self.blit_text()
        else:
            self.surface.blit(self.normal_image, self.rect)
            self.blit_text()
