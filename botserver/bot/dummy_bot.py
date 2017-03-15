import json
from . import base_bot

class DummyBot(base_bot.BaseBot):

    ability_levels = [0, 0, 0, 0, 0]
    ability_levelup_order = [0, 1, 2, 0, 0, 3, 0, 1, 1, 1]
    my_level = 1
    go_to = None
    has_moved = False

    def __init__(self):
        self.my_hero_name = 'npc_dota_hero_lina'
        super().__init__()

    ###################
    ### On requests ###
    ###################

    def on_select(self, request_json):
        return {"hero": self.my_hero_name, "command": "SELECT"}

    # returns ability number to levelup
    def on_level_up(self, request_json):
        self.my_level += 1
        return self.ability_levelup_order[self.my_level - 2]

    def on_chat_message(self, request_json):
        request_json = json.loads(request_json)
        message = request_json['text']
        message = message.split(' ')
        if message[0] == 'lina' and message[1] == 'go':
            self.go_to = message[2:5]
        return {}

    def on_update(self, request_json):
        world = json.loads(request_json)
        if self.go_to is None:
            return self.skip()
        go_to = self.go_to
        self.go_to = None
        return self.move(go_to[0], go_to[1], go_to[2])

    #def find_entities_in_range(self, world, center, range):
    #    result = world['entities'][]

    #################
    ###  COMMANDS ###
    #################

    # z is almost irrelevant, but it matters(?) when you walking near river and highground
    def move(self, x, y, z):
        return {'x': str(x), 'y': str(y), 'z': str(z), 'command': "MOVE"}

    # in on_update() you get list of entities and their status: target_id = entity number
    def attack(self, target_id):
        return {'target': target_id, 'command': "ATTACK"}

    def cast_ability(self, ability_num, target_id=None, x=None, y=None, z=None):
        if target_id is None and (x is None or y is None or z is None):
            return self.skip()
        if target_id is None:
            return { "command" : "CAST",
                     "ability" : ability_num, 
                     'x': str(x), 'y': str(y), 'z': str(z)}
        return { "command" : "CAST", "ability" : ability_num, "target" : target_id}

    # do nothing
    def skip(self):
        return {'command': 'NOOP'}