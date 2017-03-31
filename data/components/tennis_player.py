import pygame as pg
from .. import constants as c

class tennis_player(object):
    def __init__(self, game_data):
        self.game_data = game_data
        self.popularity = game_data['popularity']
        self.stats = game_data['stats']
        self.name = game_data['name']
        self.level = game_data['level']
    def get_skills(self):
        return self.stats
    def get_popularity(self):
        return self.popularity

class player(tennis_player):
    def __init__(self, game_data):
        super(player, self).__init__(game_data)
