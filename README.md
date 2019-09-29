# FFF Info Python Backend / Telegram chatbot

The Python backend for the FFF-Infopunkt website and for the FFF Infopunkt Javascript backend

## What does this service do?
* Collecting the data from telegram with a chatbot (called fffinfobot)
* Preparing the data for the dynalite backend (uses the dynamodb service) and pushing Data to server

## How to get this working
### 1. Use python3
1. Clone Repository to your local disk
2. install with `pip install telepot pynamodb`
3. Create config.json with your dynalite server and chatbot id (to use ours please use the docker version)
4. run server with `python3 bot.py`
5. Format the messages as shown below and have fun

### 2. Use docker (recommended)
1. run on an x64 machine `docker run -d pboehler/fffinfopythonbackendserver`
2. run on an arm machine like the Raspberry Pi `docker run -d pboehler/fffinfopythonbackendserver:rpi`

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

**If an element does not exists add None / none / NONE to the line**