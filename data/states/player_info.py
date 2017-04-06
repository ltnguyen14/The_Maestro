import pygame as pg
from .. import tools, setup
from .. import constants as c
from data.components import button, text_box, selection_box, tennis_player
from data.players import initialize

class menu(object):
    def __init__(self, player_name):
        self.player = tennis_player.tennis_player(player_name)
        self.pass_arg = None
        self.bg_image = setup.GFX['background_1']
        self.bg_image = pg.transform.smoothscale(self.bg_image, c.SCREEN_SIZE)

        self.position_list = {'name_box' : (45, 90),
                                'skill_info': (490, 90),
                                'attributes_title': (45, 290),
                                'attributes_box': (45, 335),

                                'physical_bt': (490, 335),
                                'technical_bt': (490, 380),
                                'mental_bt': (490, 425),

                                'upgrades_bt': (490, 495),
                                'back_bt': (490, 540)
                                }

        self.name_box = button.button(c.title_button, self.player.name, c.WHITE,
                                        self.position_list['name_box'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.skill_info = button.button(c.title_button, "SKILL INFO", c.WHITE,
                                        self.position_list['skill_info'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.attributes_title = button.button(c.title_button, "ATTRIBUTES", c.WHITE,
                                        self.position_list['attributes_title'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.attributes_box = text_box.text_box(c.attributes_box, "", c.WHITE,
                                        self.position_list['attributes_box'], "white_box", text_size = 20)

        self.physical_bt = button.button(c.title_button, "Physical Skills", c.WHITE,
                                        self.position_list['physical_bt'], "rect_box_grey", "rect_box_yellow", text_size = 20)
        self.technical_bt = button.button(c.title_button, "Technical Skills", c.WHITE,
                                        self.position_list['technical_bt'], "rect_box_grey", "rect_box_yellow", text_size = 20)
        self.mental_bt = button.button(c.title_button, "Mental Skills", c.WHITE,
                                        self.position_list['mental_bt'], "rect_box_grey", "rect_box_yellow", text_size = 20)

        self.upgrades_bt = button.button(c.title_button, "Upgrades", c.WHITE,
                                        self.position_list['upgrades_bt'], "rect_box_grey", "rect_box_yellow", text_size = 20)
        self.back_bt = button.button(c.title_button, "BACK", c.WHITE,
                                        self.position_list['back_bt'], "rect_box_grey", "rect_box_yellow", text_size = 20)


        self.buttons = (self.name_box, self.skill_info, self.attributes_title,
                    self.physical_bt, self.technical_bt, self.mental_bt, self.attributes_box,
                    self.upgrades_bt, self.back_bt)

        self.highlight_attribute = 'Physical Skills'
        self.surface = pg.display.get_surface()
        self.create_dynamic_buttons()
        self.choose_dynamic_buttons(self.highlight_attribute)

    def startup(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    def create_dynamic_buttons(self):
        atribute_position = {'attribute 1': (50, 350),
                                'attribute 2': (50, 385),'attribute 3': (50, 420),
                                'attribute 4': (50, 455),'attribute 5': (50, 490),
                                'info_box' : (490, 135)
        }

        self.physical_stats = self.player.stats['physical']
        self.technical_stats = self.player.stats['skill']
        self.mental_stats = self.player.stats['mental']

        self.power_bt = button.button(c.attribute_small, "Power: " + str(self.physical_stats['Power']), c.WHITE,
                                        atribute_position['attribute 1'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.stamina_bt = button.button(c.attribute_small, "Stamina: " + str(self.physical_stats['Stamina']), c.WHITE,
                                        atribute_position['attribute 2'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.top_speed_bt = button.button(c.attribute_small, "Top Speed: " + str(self.physical_stats['Top Speed']), c.WHITE,
                                        atribute_position['attribute 3'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.acceleration_bt = button.button(c.attribute_small, "Acceleration: " + str(self.physical_stats['Acceleration']), c.WHITE,
                                        atribute_position['attribute 4'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.reflexes_bt = button.button(c.attribute_small, "Reflexes: " + str(self.physical_stats['Reflexes']), c.WHITE,
                                        atribute_position['attribute 5'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.physical_info = button.button(c.info_box, "", c.BLACK,
                                        atribute_position['info_box'], "white_box", "white_box", text_size = 20)

        self.forehand_bt = button.button(c.attribute_small, "Forehand: " + str(self.technical_stats['Forehand']), c.WHITE,
                                        atribute_position['attribute 1'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.backhand_bt = button.button(c.attribute_small, "Backhand: " + str(self.technical_stats['Backhand']), c.WHITE,
                                        atribute_position['attribute 2'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.volley_bt = button.button(c.attribute_small, "Volley: " + str(self.technical_stats['Volley']), c.WHITE,
                                        atribute_position['attribute 3'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.serve_bt = button.button(c.attribute_small, "Serve: " + str(self.technical_stats['Serve']), c.WHITE,
                                        atribute_position['attribute 4'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.technical_info = button.button(c.info_box, "", c.BLACK,
                                        atribute_position['info_box'], "white_box", "white_box", text_size = 20)

        self.m_toughness_bt = button.button(c.attribute_small, "Mental Toughness: " + str(self.mental_stats['Mental Toughness']), c.WHITE,
                                        atribute_position['attribute 1'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.m_durability_bt = button.button(c.attribute_small, "Mental Durability: " + str(self.mental_stats['Mental Durability']), c.WHITE,
                                        atribute_position['attribute 2'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.m_acceleration_bt = button.button(c.attribute_small, "Mental Acceleration: " + str(self.mental_stats['Mental Acceleration']), c.WHITE,
                                        atribute_position['attribute 3'], "rect_box_grey", "rect_box_grey", text_size = 20)
        self.mental_info = button.button(c.info_box, "", c.BLACK,
                                        atribute_position['info_box'], "white_box", "white_box", text_size = 20)

        self.physical_bts = (self.power_bt, self.stamina_bt, self.top_speed_bt, self.acceleration_bt, self.reflexes_bt, self.physical_info)
        self.technical_bts = (self.forehand_bt, self.backhand_bt, self.volley_bt, self.serve_bt, self.technical_info)
        self.mental_bts = (self.m_toughness_bt, self.m_durability_bt, self.m_acceleration_bt, self.mental_info)

    def choose_dynamic_buttons(self, highlight_attribute):
        self.highlight_attribute = highlight_attribute
        if self.highlight_attribute == "Physical Skills":
            self.highlight_attribute_bts = self.physical_bts
        elif self.highlight_attribute == "Technical Skills":
            self.highlight_attribute_bts = self.technical_bts
        elif self.highlight_attribute == "Mental Skills":
            self.highlight_attribute_bts = self.mental_bts

    def update(self, mouse_state, mouse_pos):
        self.surface.blit(self.bg_image, (0,0))
        #Update buttons
        for button in self.buttons + self.highlight_attribute_bts:
            if button.rect.collidepoint(mouse_pos):
                button.highlight = True
                result = button.update(mouse_state, mouse_pos)
                self.check_mouse_click(result)
            else:
                button.highlight = False
                button.draw()

    def check_mouse_click(self, result):
        if result in ('Physical Skills', 'Technical Skills', 'Mental Skills'):
            self.choose_dynamic_buttons(result)
