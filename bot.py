import telepot from telepot.delegate import per_chat_id
import create_open
import pave_event_space
import include_callback_query_chat_id import json import Strike import time def telegramBot():
    datasets = []
    datasetsOld = []
    id = 1  # counter var
    updateIdOld = 0  # no updates fetched
    print("Listening....")
    while True:
        # load config files
        data = json.load(open('config.json'))
        telegram_bot_token = data['bot']['private_key']
        # get the old update Id if it exists
        updateIdOld = data['bot']['updateId']
        bot = telepot.Bot(telegram_bot_token)
        if updateIdOld == 0:
            updates = bot.getUpdates()
            if len(updates) != 0:
                updateIdOld = updates[len(updates)-1]['update_id']
            else:
                #print("There are no updates available")
                continue
        else:
            updates = bot.getUpdates(updateIdOld + 1)
            if len(updates) != 0:
                updateIdOld = updates[len(updates) - 1]['update_id']
            else:
                #print("There are no updates available")
                continue
        with open('config.json', mode='w') as json_data_file:  # add the new id to file
            #data = json.load(json_data_file)
            data['bot']['updateId'] = updateIdOld
            try:
                # write data to file, if it fails, catch error
                json_data_file.write(json.dumps(data))
            except:
                print(str(time.time()) + ": Error while writing file, please check your permsissions! (need to be "
                                         "read write (chmod 777 config.json)")  # time in milliseconds until the 1.1.1970
            json_data_file.close()
        # print(updates)
        messages = dict()
        groupIds = [update['message']['chat']['id']
                    for update in updates if 'text' in update['message']]
        groupNames = [groupName['message']['chat']['title']
                      for groupName in updates if 'text' in groupName['message']]
        for groupId in groupIds:
            messages[str(groupId)] = [update['message']['text'] for update in updates if 'text' in update['message']
                                      and groupId == update['message']['chat']['id']]
        datasets = []
        i = 0
        for messageSet in messages.values():
            chatId = groupIds[i]
            title = ""
            description = ""
            dateTime = ""
            startingPoint = ""
            startingTime = ""  # could be a time stamp is a UnicodeAttribute now!
            endPoint = ""
            routeLength = ""
            jsonFeed = []
            for message in messageSet:
                # TODO Fix help message to only be displayed once
                if (message == "help"):
                    bot.sendMessage(text="Jedes “Property in einer Zeile”\nWenn nicht bekannt NONE "
                                         "einfügen\n\nSchema:\nTitel\nBeschreibung\nDatum und Uhrzeit\nStartpunkt / "
                                         "Treffpunkt\nEndpunkt\nRoutenlänge\nWebsite Veranstalter (wenn nicht bekannt "
                                         "NONE schreiben)\n", chat_id=chatId)
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
                            # meetingPoint / StartPoint
                            if jsonFeed[6].lower().strip() == 'none':
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
        # print(datasets)
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
            print("Stored!")
            id += 1
        datasetsOld = datasets
        print(datasets)
        print("Wrote data to server") if "__main__":
    telegramBot()
