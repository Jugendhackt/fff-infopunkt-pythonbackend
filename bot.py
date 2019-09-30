import telepot
import json
import Strike
import logger


def telegramBot():
    datasetsOld = []
    id = 1  # counter var

    logger.writeLine("Listening....")

    while True:
        # load config files
        data = json.load(open('config.json'))

        telegram_bot_token = data['bot']['private_key']
        updateIdOld = data['bot']['updateId']  # get the old update Id if it exists
        bot = telepot.Bot(telegram_bot_token)

        if updateIdOld == 0:
            updates = bot.getUpdates()
            if len(updates) != 0:
                updateIdOld = updates[len(updates) - 1]['update_id']
            else:
                continue
        else:
            updates = bot.getUpdates(updateIdOld + 1)
            if len(updates) != 0:
                updateIdOld = updates[len(updates) - 1]['update_id']
            else:
                continue

        with open('config.json', mode='w') as json_data_file:  # add the new id to file
            data['bot']['updateId'] = updateIdOld
            try:
                json_data_file.write(json.dumps(data))  # write data to file, if it fails, catch error
            except:
                logger.writeLine("Error while writing file, please check your permissions! (need to be "
                                 "read write (chmod 777 config.json)")  # time until the 1.1.1970 in ms
            json_data_file.close()

        messages = dict()

        groupIds = [update['message']['chat']['id'] for update in updates if 'text' in update['message']]
        groupNames = [groupName['message']['chat']['title'] for groupName in updates if 'text' in groupName['message']]

        for groupId in groupIds:
            messages[str(groupId)] = [update['message']['text'] for update in updates if 'text' in update['message']
                                      and groupId == update['message']['chat']['id']]

        datasets = []
        i = 0
        for messageSet in messages.values():

            chatId = groupIds[i]

            for message in messageSet:
                # TODO Fix help message to only be displayed once
                if message == "help":
                    bot.sendMessage(text="Jedes “Property in einer Zeile”\nWenn nicht bekannt NONE "
                                         "einfügen\n\nSchema:\nTitel\nBeschreibung\nDatum und Uhrzeit\nStartpunkt / "
                                         "Treffpunkt\nEndpunkt\nRoutenlänge\nWebsite Veranstalter (wenn nicht bekannt "
                                         "NONE schreiben)\n", chat_id=chatId)
                    continue
                if message == "log":
                    bot.sendMessage(text=logger.readLogs(), chat_id=chatId)  # send logs with bot
                    continue

                try:
                    jsonFeed = message.split('\n')
                    if len(jsonFeed) == 10:
                        if jsonFeed[0].lower().strip() == 'bot:':
                            if jsonFeed[1].lower().strip() == 'none':  # Title
                                jsonFeed[1] = ' '
                            if jsonFeed[2].lower().strip() == 'none':  # Description
                                jsonFeed[2] == ' '
                            if jsonFeed[3].lower().strip() == 'none':  # organisation
                                jsonFeed[3] = ' '
                            if jsonFeed[4].lower().strip() == 'none':  # Date
                                jsonFeed[4] = ' '
                            if jsonFeed[5].lower().strip() == 'none':  # Time
                                jsonFeed[5] = ' '
                            if jsonFeed[6].lower().strip() == 'none':  # meetingPoint / StartPoint
                                jsonFeed[6] = ' '
                            if jsonFeed[7].lower().strip() == 'none':  # endPoint
                                jsonFeed[7] = ' '
                            if jsonFeed[8].lower().strip() == 'none':  # routing
                                jsonFeed[8] = ' '
                            if jsonFeed[9].lower().strip() == 'none':  # url
                                jsonFeed[9] = ' '
                            else:
                                jsonFeed[9] = "https://" + jsonFeed[9]
                            datasets.append(jsonFeed)

                except:
                    continue

        if datasets == datasetsOld:
            continue

        for dataset in datasets:
            print(dataset)

            model = Strike.StrikeModel()
            model.title = dataset[1]
            model.description = dataset[2]
            model.organisation = dataset[3]
            model.date = dataset[4]
            model.startTime = dataset[5]
            model.meetingPoint = dataset[6]
            model.endPoint = dataset[7]
            model.routeLength = dataset[8]
            model.url = dataset[9]
            model.groupSource = "FFF Info Test Group"
            model.source = "Telegram chat group, collected bei FFF_Info Bot"
            model.latitude = 0
            model.longitude = 0
            model.searchTitle = dataset[1].lower()
            model.strikeId = id

            model.save()
            id += 1

        datasetsOld = datasets
        # print(datasets)
        logger.writeLine("Wrote data to server")


if "__main__":
    telegramBot()
