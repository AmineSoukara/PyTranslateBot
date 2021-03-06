# (c) @AmineSoukara

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = int(os.environ.get("UPDATES_CHANNEL"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))