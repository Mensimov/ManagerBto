from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


APP_ID = config('APP_ID',default=None,cast=int)
API_HASH = config('API_HASH',default=None)
BOT_TOKEN = config('BOT_TOKEN',default=None)
ADMIN = config('ADMIN',default=None,cast=int)
KANAL = config('KANAL',default=None,cast=int)
ADMIN_USERNAME = config('ADMIN_USERNAME',default=None)
KANAL_USERNAME = config('KANAL_USERNAME',default=None)

klent = TelegramClient('ManagerBto', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)