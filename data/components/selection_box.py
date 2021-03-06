import pygame as pg
from .. import setup
from .. import constants as c

class menu(object):
    def __init__(self, size, text_list, text_color, position, normal_box, hl_box, center=False, text_size=30):
        self.text_list = text_list
        self.index = 0
        self.text_color = text_color
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

        self.normal_font = pg.font.Font(setup.FONTS['AllerDisplay'], text_size)
        self.value = self.text_list[self.index]

    def blit_text(self):
        self.label = self.normal_font.render(self.text_list[self.index], 1, self.text_color)
        self.label_rect = self.label.get_rect()
        self.label_rect.center = self.rect.center

        self.surface.blit(self.label, self.label_rect)

    def update(self, mouse_state, mouse_pos):
        self.draw()
        if mouse_state[0]:
            if mouse_pos[0] < self.rect.x + self.rect.width/4:
                self.index -= 1
                self.index = self.index % len(self.text_list)
                self.value = self.text_list[self.index]
                return self.value
            if mouse_pos[0] > self.rect.x + 3*self.rect.width/4:
                self.index += 1
                self.index = self.index % len(self.text_list)
                self.value = self.text_list[self.index]
                return self.value


    def draw(self):
        if self.highlight:
            self.surface.blit(self.hl_image, self.rect)
            self.blit_text()
        else:
            self.surface.blit(self.normal_image, self.rect)
            self.blit_text()
