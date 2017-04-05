import pygame as pg
import pickle, os
from .. import constants as c

class tennis_player(object):
    def __init__(self, player_name):
        self.game_data = self.create_game_data(player_name)
        self.popularity = self.game_data['popularity']
        self.stats = self.game_data['stats']
        self.name = self.game_data['name']
        self.level = self.game_data['level']

    def create_game_data(self, player_name):
        player_db = pickle.load( open( os.path.join("data", "players", c.player_file), "rb" ) )
        return player_db[player_name]

class player(tennis_player):
    def __init__(self, game_data):
        super(player, self).__init__(game_data)
