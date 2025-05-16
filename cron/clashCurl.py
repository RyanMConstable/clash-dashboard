import requests
from urllib.parse import quote
from sqlalchemy import Table, Column, MetaData, Integer, Computed, event, create_engine, select, insert
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timezone
import os

TOK = os.getenv("TOK")

HEADERS = {"Authorization": f"Bearer {TOK}"}
#engine = create_engine("postgresql://postgres:changeme@db:5432/cocdb")
engine = create_engine("postgresql://postgres:changeme@localhost:5432/cocdb")

metadata = MetaData()

def updateHistoryTables():
    now = datetime.now()

    userinfo = Table("userinfo", metadata, autoload_with=engine)
    clanlist = Table("clanlist", metadata, autoload_with=engine)

    users = {}
    clans = []

    with engine.connect() as conn:
        result = conn.execute(select(userinfo))
        for row in result:
            if row[1] not in users:
                users[row[1]] = row[2]
        result = conn.execute(select(clanlist))
        for row in result:
            clans.append(row[1])

    #users is in the format {PLAYERTAG: PHONENUMBER}
    playerhistory = Table("playerhistory", metadata, autoload_with=engine)
    clanhistory = Table("clanhistory", metadata, autoload_with=engine)
    with engine.connect() as conn:

        playerClans = set()

        for user in users:
            encodedUser = quote(user)
            url = f"https://api.clashofclans.com/v1/players/{encodedUser}"
            result = requests.get(url, headers=HEADERS)
            if result.status_code != 200:
                print(f"[ERROR]: Status code: {result.status_code}")
                continue
        
            json = result.json()
            clantag = json['clan']['tag']
            playerClans.add(clantag)

            insertDict = {}
            #Here is where we take the json and set up the insert dictionary
            insertDict['time'] = now
            insertDict['playertag'] = user
            insertDict['townhalllevel'] = json['townHallLevel']
            if 'townHallWeaponLevel' in json:
                insertDict['townhallweaponlevel'] = json['townHallWeaponLevel']
            else:
                insertDict['townhallweaponlevel'] = 0
            insertDict['explevel'] = json['expLevel']
            insertDict['trophies'] = json['trophies']
            insertDict['besttrophies'] = json['bestTrophies']
            insertDict['warstars'] = json['warStars']
            insertDict['attackwins'] = json['attackWins']
            insertDict['defensewins'] = json['defenseWins']
            insertDict['builderhalllevel'] = json['builderHallLevel']
            insertDict['builderbasetrophies'] = json['builderBaseTrophies']
            insertDict['bestbuilderbasetrophies'] = json['bestBuilderBaseTrophies']
            insertDict['role'] = json['role']
            insertDict['warpreference'] = json['warPreference']
            insertDict['donations'] = json['donations']
            insertDict['donationsreceived'] = json['donationsReceived']
            insertDict['clancapitalcontributions'] = json['clanCapitalContributions']
            insertDict['league'] = json['league']['name']
            insertDict['builderleague'] = json['builderBaseLeague']['name']
            insertDict['clantag'] = json['clan']['tag']

            conn.execute(insert(playerhistory), insertDict)
            conn.commit()

        for clan in playerClans:
            if clan not in clans:
                clans.append(clan)
                conn.execute(insert(clanlist), {'clantag':f'{clan}'})
                conn.commit()

        clans = list(set(clans))

        for clan in clans:
            encodedClan = quote(clan)
            url = f"https://api.clashofclans.com/v1/clans/{encodedClan}"
            result = requests.get(url, headers=HEADERS)
            if result.status_code != 200:
                print(f"[ERROR]: Status code: {result.status_code}")
                continue
           
            json = result.json()

            insertDict = {}

            insertDict["time"] =  now
            insertDict["clantag"] = json["tag"]
            insertDict["description"] = json["description"]
            insertDict["clanlevel"] = json["clanLevel"]
            insertDict["clanpoints"] = json["clanPoints"]
            insertDict["clanbuilderbasepoints"] = json["clanBuilderBasePoints"]
            insertDict["clancapitalpoints"] = json["clanCapitalPoints"]
            insertDict["capitalleague"] = json["capitalLeague"]["name"]
            insertDict["warwinsstreak"] = json["warWinStreak"]
            insertDict["warwins"] = json["warWins"]
            insertDict["warties"] = json["warTies"]
            insertDict["warlosses"] = json["warLosses"]
            insertDict["warleague"] = json["warLeague"]["name"]
            insertDict["members"] = json["members"]
            insertDict["location"] = json["location"]["name"]
            insertDict["requiredtrophies"] = json["requiredTrophies"]

            conn.execute(insert(clanhistory), insertDict)
            conn.commit()

def warUpdates():
    now = datetime.now()

    clans = []

    clanlist = Table("clanlist", metadata, autoload_with=engine)

    with engine.connect() as conn:
        result = conn.execute(select(clanlist))
        for row in result:
            clans.append(row[1])

    for clan in clans:
        encodedClan = quote(clan)
        url = f"https://api.clashofclans.com/v1/clans/{encodedClan}/currentwar"
        result = requests.get(url, headers=HEADERS)
        if result.status_code != 200:
            print(f"[ERROR]: Status code: {result.status_code}")
        
    json = result.json()

    if json["state"] != "inWar":
        print("Clan not in war")
        return
    
    pk = json["startTime"] + json["clan"]["tag"]

    return

scheduler = BlockingScheduler()
scheduler.add_job(updateHistoryTables, 'interval', seconds=900)
scheduler.start()
