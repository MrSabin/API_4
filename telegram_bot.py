import os

import telegram
from dotenv import load_dotenv

load_dotenv()
token = os.environ["TELEGRAM_TOKEN"]
bot = telegram.Bot(token=token)
chat_id = -1001522793852
bot.send_document(chat_id=chat_id, document=open('images/test.jpg', 'rb'))
