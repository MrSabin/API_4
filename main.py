import argparse
import os
import random
import time
from pathlib import Path

from dotenv import load_dotenv
from telegram_bot import send_photo


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--delay", default=14400, help="Задержка между отправками в секундах"
    )
    args = parser.parse_args()

    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    env_delay = os.getenv("DELAY_SECONDS")
    delay = args.delay if env_delay is None else env_delay
    print("Scanning folder for images...")
    path = Path.cwd() / "images"
    image_paths = []
    files = os.listdir(path)
    for file in files:
        image_paths.append(os.path.join(path, file))

    while True:
        for image_path in image_paths:
            print("Sending image...")
            send_photo(image_path, token, chat_id)
            print(f"Sended image. Waiting {delay} seconds for next iteration.")
            time.sleep(int(delay))
        random.shuffle(image_paths)


if __name__ == "__main__":
    main()
