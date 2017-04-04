import pygame as pg
from .. import tools, setup
from .. import constants as c
from data.components import button, text_box, selection_box
from data.players import initialize

class menu(object):
    def __init__(self, input_arg):
        initialize.run()
        self.input_arg = input_arg
        self.pass_arg = None
        self.bg_image = setup.GFX['background_1']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'title' : (c.SCREEN_WIDTH/2, 50)}

        self.title = button.button(c.info_button_sz, self.input_arg, c.BLUE,
                                        self.position_list['title'], "rect_box_grey", "rect_box_grey", center=True, text_size = 20)

        self.buttons = (self.title,)

        self.surface = pg.display.get_surface()

    def startup(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def update(self, mouse_state, mouse_pos):
        self.surface.blit(self.bg_image, (0,0))
        #Update buttons
        for button in self.buttons:
            if button.rect.collidepoint(mouse_pos):
                button.highlight = True
                result = button.update(mouse_state, mouse_pos)
                self.check_mouse_click(result)
            else:
                button.highlight = False
                button.draw()

    def check_mouse_click(self, result):
        if result == 'BACK':
            self.next = 'welcome_screen'
            self.done = True
        elif result == 'NEXT':
            self.next = 'player_info'
            self.pass_arg = 'player'
            self.done = True
