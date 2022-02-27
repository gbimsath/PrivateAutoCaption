# <C> MoTechYT


import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    CAPTION = os.environ.get("CAPTION", "")
    BUTTON_TEXT = os.environ.get("BUTTON", "🔻Join Channel🔻")
    GROUP_LINK = os.environ.get("GROUP_LINK", "https://t.me/+rWHmdVt3NythYzI1")
    CHANNEL_LINK = os.eviron.get("CHANNEL_LINK")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "https://t.me/MOHLK_MG_UPDATES")
