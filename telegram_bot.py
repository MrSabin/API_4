import os

import telegram
from dotenv import load_dotenv

load_dotenv()
token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["CHAT_ID"]
bot = telegram.Bot(token=token)


def send_photo(image_path):
    bot.send_document(chat_id=chat_id, document=open(image_path, 'rb'))
