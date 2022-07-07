import telegram


def send_photo(image_path, token, chat_id):
    bot = telegram.Bot(token=token)
    with open(image_path, 'rb') as photo:
        bot.send_document(chat_id=chat_id, document=photo)
