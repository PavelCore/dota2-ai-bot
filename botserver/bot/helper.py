from .dummy_bot import DummyBot


bot = DummyBot()


def initialize_bot():
    if bot is None:
        bot = DummyBot()
    return bot


def get_bot():
    if bot is None:
        return initialize_bot()
    return bot
