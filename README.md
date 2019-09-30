 ![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg) ![docker](https://img.shields.io/badge/Docker-We%20use%20Docker-blue) ![JugendHackt](https://img.shields.io/badge/JugendHackt-made%20with%20%3C3-success=)

# FFF Info Python Backend / Telegram chatbot
![logo](logo.png)

The Python backend for the FFF-Infopunkt website and for the FFF Infopunkt Javascript backend

## What does this service do?
* Collecting the data from telegram with a chatbot (called fffinfobot)
* Preparing the data for the dynalite backend (uses the dynamodb service) and pushing Data to server

## How to get this working
### 1. Use python3
1. Clone Repository to your local disk
2. Install with `pip install telepot pynamodb`
3. Create config.json with your dynalite server and chatbot id (to use ours please use the docker version), the config
file is needed because we are getting the api keys from this file:
Please format the file in the following way:
*config.json:*
``` json
{
  "bot": {
    "private_key": "botprivatekey",
    "updateId": 0
  },
  "aws": {
    "access_key": "awsaccesskey",
    "private_key": "privatekey",
    "region": "region"
  }
}
```
4. Run server with `python3 bot.py`
5. Format the messages as shown below and have fun

### 2. Use docker (recommended)
1. Run on an x64 machine `docker run -d pboehler/fffinfopythonbackendserver`
2. Run on an arm machine like the Raspberry Pi `docker run -d pboehler/fffinfopythonbackendserver:rpi`

## Format the messages:
The messages need to be formated with the following pattern:
1. bot:
2. A title
3. A short description (need to be one line)
4. The organisation
5. The date
6. The start time
7. The meeting point / starting point
8. The end point
9. A website url

**The 'bot:' statement is needed to let the bot know that the message is meant for him / her**

**If an element does not exists add 'None' / 'none' / 'NONE' to the line**

## Other informations about running the system:
* We are writing log files, you can view them in file logger.log. The timestamp is counted in Milliseconds from the 01.01.1970 (you can easily convert them with bash)
* Our server at the moment only runs with 0.5 Gb of RAM (so not that much), so please don't send a million messages at once

## Planned for future:
* Integration to more chat services
* Email
* ML for text recognition
