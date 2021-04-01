from telethon import TelegramClient
from decouple import config
import logging
import time
import sqlite3

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

con = sqlite3.connect('user.db')
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (msgid INT, userid INT, ad TEXT)")
def add_to_db(msgid,userid,ad):
	cursor.execute(f"INSERT INTO users VALUES ({msgid},{userid},'{ad}')")
	con.commit()

APP_ID = config('APP_ID',default=None,cast=int)
API_HASH = config('API_HASH',default=None)
BOT_TOKEN = config('BOT_TOKEN',default=None)
ADMIN = config('ADMIN',default=None,cast=int)
KANAL = config('KANAL',default=None,cast=int)
ADMIN_USERNAME = config('ADMIN_USERNAME',default=None)
KANAL_USERNAME = config('KANAL_USERNAME',default=None)

klent = TelegramClient('ManagerBto', APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
