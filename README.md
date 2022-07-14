# Space Telegram
This project contains scripts for:
- Download SpaceX photos of last launch/launch by ID (fetch_spacex_images.py)
- Download specified amount of photos from NASA APOD service (fetch_nasa_apod.py)
- Download Earth photos from NASA EPIC service (fetch_nasa_epic.py)
- Send downloaded photos to Telegram chat with specified delay (main.py)

## How to install

1. Download repository

2. Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```python
pip install -r requirements.txt
```

## Setting up

For use this scripts, you will need:
- Telegram bot token (use existing one or create new on [@BotFather](http://t.me/BotFather))
- NASA API token, get it on [NASA API](https://api.nasa.gov)
- Your Telegram chat ID

Create .env file in script directory, then put in your tokens and parameters, like:
```python
NASA_TOKEN="your_nasa_api_token"
TELEGRAM_TOKEN="your_telegram_bot_token"
TELEGRAM_CHAT_ID="your_chat_id"
DELAY_TIME="desired_delay_time"
```

## Using scripts

1. Download SpaceX photos:
Run script by typing
```python
python3 fetch_spacex_images.py
```
This will download photos from SpaceX last lauch. If you want photos from specified launch - run script with `--id` parameter, like
```python
python3 fetch_spacex_images.py --id "launch_id"
```
Script will download photos to `images/` subdir in script directory.

2. Download NASA APOD photos:
Run script by typing
```python
python3 fetch_nasa_apod.py -count 'how_many_photos'
```
This will download specified amount of photos from NASA Picture of a Day project. Script will download photos to `images/` subdir in script directory.

3. Download NASA EPIC photos:
Run script by typing
```python
python3 fetch_nasa_epic.py
```
This will download photos from NASA EPIC project. Script will download photos to `images/` subdir in script directory.

4. Sending photos to Telegram:
After you downloaded all photos, you can start script for automatic posting with Telegram bot. Run script by typing
```python
python3 main.py
```
Script will post photos from `images/` folder with delay, specified in .env file (DELAY_TIME) or by running script with `--delay` argument, like
```python
python3 main.py --delay "delay_in_seconds"
```
Delay time should be entered in seconds.

