class BaseBot():
    
    name = "base_bot"

    def __init__(self):
        pass

    def on_chat_message(self, request_json):
        return {}

    def on_level_up(self, request_json):
        return {'abilityIndex': -1}

    def on_update(self, request_json):
        return {}

    def on_reset(self, request_json):
        return {}
