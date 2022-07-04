import os

import telegram
from dotenv import load_dotenv

load_dotenv()
token = os.environ["TELEGRAM_TOKEN"]
bot = telegram.Bot(token=token)
bot.send_message(text='Hello world!', chat_id=-1001522793852)
