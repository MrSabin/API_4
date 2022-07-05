import argparse
import os
import random
import time

from dotenv import load_dotenv
from telegram_bot import bot_send_photo

parser = argparse.ArgumentParser()
parser.add_argument('--delay', help='Задержка между отправками в секундах')
args = parser.parse_args()

load_dotenv()
delay = args.delay if args.delay else os.environ["DELAY_TIME"]


def main():
    print("Scanning folder for images...")
    path = "images/"
    image_paths = []
    files = os.listdir(path)
    for file in files:
        image_paths.append(os.path.join(path, file))

    while True:
        for image_path in image_paths:
            print("Sending image...")
            bot_send_photo(image_path)
            print(f"Sended image. Waiting {delay} seconds for next iteration.")
            time.sleep(int(delay))
        random.shuffle(image_paths)


if __name__ == '__main__':
    main()
