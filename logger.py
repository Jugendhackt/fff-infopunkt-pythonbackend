import json
import time

def writeLine(content):
    file = open("logger.log", mode="a")
    file.write(str(time.time()) + ": " + content)
    file.close()

def readLogs():
    with open("logger.log", "r") as file:
        data = file.readlines()
        return data