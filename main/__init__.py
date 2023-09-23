#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("27825018", default=None, cast=int)
API_HASH = config("1f15c46306107d21be901af5c8baf9bc", default=None)
BOT_TOKEN = config("6640491258:AAH3e0xTJr6BM9cadCtviWWGebVSnM9Q-YI", default=None)
SESSION = config("BQCFa9TAvzx73xhDYqC_mpr7wav69xTU4hA83GJeRtSStx8870wk7JRw5x_WKx6B9U5Ae47Q0_5FlJQ7ikpm41E64yar8N0gDJ15NinumLSczmxDHUBai5b4QhjNzE1VcbemOjUeWt811iRncgrQNPfFhvJ1uJbLj2cKIdiWcUeJ0r4BNrm3ORhaF8u96FuloTtTYxKRJXRKOUycXmzk-t1v8fuettNiExQsumFl-6JUo8oBPYhlObDClbxN-cIR4y7XagJiHPXgrAtZaedfUknwx2rfVoKJNRQtgAgok17DAIA8skGe5XBMzT-Z0hp_w6nmfMnvBBsSj3wNT7TXmVcuAAAAAVY5hCoA", default=None)
FORCESUB = config("meracourse123", "" default=None)
AUTH = config("5741577258", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
