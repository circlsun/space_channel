# Space Telegram

[TODO: here would be project description]

### How to install

[TODO: tell user where he should get keys, where they should be and how they look like]

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## Virtual envs

NASA will not give you the data until you receive a personal "apikey". It is needed to interact with the NASA API.
The link to generate the token is listed on the API NASA [Getting Started](https://api.nasa.gov/)

The received apikey must be placed in the ".env" file as `APYKEY="insert you apikey"`.
```
/user/space_channel/
|--foo1.py
|--foo2.py
|--.env
```
If the token is not in the ".env" file, the result will be:
```
Add an apikey from NASA to the virtual environment file <.env>
```

### Project Goals

The code is written for educational purposes for the online-course of the Web Services API on [Devmen](https://dvmn.org/)