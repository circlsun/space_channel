# Space Telegram-Bot

This is a set of several scripts for collecting and publishing photos of space in a telegram bot

## How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## Virtual envs

`.env` file contents:

```
APIKEY = '3K*************************'
TELEGRAM_TOKEN = '5******************'
TELEGRAM_CHAT_ID = '*********'
FRIQUENCY = '4'
```
`APIKEY`: NASA will not give you the data until you receive a personal "apikey". It is needed to interact with the NASA API. The link to generate the token is listed on the API NASA [Getting Started](https://api.nasa.gov/)

`TELEGRAM_TOKEN`: You also need to create a Telegram bot. To do this, contact [BotFather](https://telegram.me/BotFather).

`TELEGRAM_CHAT_ID` is a link to a public Telegram channel in which photos will be published.

`FRIQUENCY` - pause of publications in hours.

```
/user/space_channel/
|--foo.py
|  :
|--bare.py
|--.env


```
If apikey is not in the ".env" file, the result will be:
```
Add apikey from NASA to the virtual environment file <.env>
```
## Usage

### fetch_nasa_apod.py

Uploads via [API NASA](https://api.nasa.gov/) a set of 30 space photos from [NASA Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html/) to the `/images` directory (creates it if not present).

### fetch_nasa_epic.py

Uploads via [API NASA](https://api.nasa.gov) a set of 30 space photos from [NASA Astronomy Picture of the Day]([NASA EPIC](https://epic.gsfc.nasa.gov/)) to the `/images` directory (creates it if not present).

### fetch_spacex_images.py
### telegram_bot_single.py
### telegram_bot.py

## Project Goals

The code is written for educational purposes for the online-course of the Web Services API on [Devmen](https://dvmn.org/)