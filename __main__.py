import sys
import bot
import logger
import threading


def main():
    print("Hallo")
    logger.writeLine("Started bot")
    telegramBotThread = threading.Thread
    telegramBotThread.run(bot.telegramBot())


if "__main__":
    main()
