import time

import telegram


def send_photo(image_path, token, chat_id):
    bot = telegram.Bot(token=token)
    with open(image_path, 'rb') as photo:
        try:
            bot.send_document(chat_id=chat_id, document=photo)
        except telegram.error.NetworkError:
            print("Network error occured. Retrying in 10 seconds...")
            time.sleep(10)
            send_photo(image_path, token, chat_id)
