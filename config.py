# <C> MoTechYT


import os

class Config(object):
    MT_BOT_TOKEN = os.environ.get("MT_BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    URL_LINK = os.environ.get("LINK", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
