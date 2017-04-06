import pickle, os
from .. import constants as c

def run():
    ############################### PLAYER
    player_skill = {
        'Forehand':30,
        'Backhand':30,
        'Volley':30,
        'Serve':30
    }
    player_physical = {
        'Power':30,
        'Stamina':30,
        'Top Speed':30,
        'Acceleration':30,
        'Reflexes':30,
    }
    player_mental = {
        'Mental Toughness':30,
        'Mental Durability':30,
        'Mental Acceleration':30,
    }

    ############################### ADAM
    adam_skill = {
        'Forehand':30,
        'Backhand':30,
        'Volley':30,
        'Serve':30
    }
    adam_physical = {
        'Power':30,
        'Stamina':30,
        'Top Speed':30,
        'Acceleration':30,
        'Reflexes':30,
    }
    adam_mental = {
        'Mental Toughness':30,
        'Mental Durability':30,
        'Mental Acceleration':30,
    }
    ############################### BOB
    bob_skill = {
        'Forehand':30,
        'Backhand':30,
        'Volley':30,
        'Serve':30
    }
    bob_physical = {
        'Power':30,
        'Stamina':30,
        'Top Speed':30,
        'Acceleration':30,
        'Reflexes':30,
    }
    bob_mental = {
        'Mental Toughness':30,
        'Mental Durability':30,
        'Mental Acceleration':30,
    }

    ###############################
    player = {'name': 'Player',
            'age': 15,
            'stats': {'skill': player_skill, 'physical': player_physical, 'mental': player_mental},
            'level': 'high school',
            'popularity': None
            }
    adam = {'name': 'Adam',
            'age': 16,
            'stats': {'skill': adam_skill, 'physical': adam_physical, 'mental': adam_mental},
            'level': 'high school',
            'popularity': None
            }
    bob = {'name': 'Bob',
            'age' : 17,
            'stats': {'skill': bob_skill, 'physical': bob_physical, 'mental': bob_mental},
            'level': 'high school',
            'popularity': None
            }
    ###############################
    player_data = {'player':player, 'adam':adam, 'bob': bob}

    file_obj = open(os.path.join("data", "players", c.player_file), "wb")
    pickle.dump(player_data, file_obj)

    file_obj.close()

if __name__ == '__main__':
    run()
