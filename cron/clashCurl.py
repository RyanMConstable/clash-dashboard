import requests
from urllib.parse import quote
from sqlalchemy import Table, Column, MetaData, Integer, Computed, event, create_engine, select, insert, update
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timezone
import os

TOK = os.getenv("TOK")

HEADERS = {"Authorization": f"Bearer {TOK}"}
engine = create_engine("postgresql://postgres:changeme@db:5432/cocdb")

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
            print(json)
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
            if 'league' in json:
                insertDict['league'] = json['league']['name']
            else:
                insertDict['league'] = 'None'
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
    clans = []
    warExists = False

    clanlist = Table("clanlist", metadata, autoload_with=engine)
    clanwars = Table("clanwars", metadata, autoload_with=engine)
    playerwarattacks = Table("playerwarattacks", metadata, autoload_with=engine)

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

            result = conn.execute(select(clanwars).where(clanwars.c.id == pk)).first() 

            print(result)
            if result != None:
                warExists = True

            insertDict = {}

            insertDict["id"] = pk
            insertDict["teamsize"] = json["teamSize"]
            insertDict["attackspermember"] = json["attacksPerMember"]
            insertDict["battlemodifier"] = json["battleModifier"]

            insertDict["clanlevel"] = json["clan"]["clanLevel"]
            insertDict["attacks"] = json["clan"]["attacks"]
            insertDict["stars"] = json["clan"]["stars"]
            insertDict["destructionpercentage"] = json["clan"]["destructionPercentage"]

            insertDict["enemyclanlevel"] = json["opponent"]["clanLevel"]
            insertDict["enemyattacks"] = json["opponent"]["attacks"]
            insertDict["enemystars"] = json["opponent"]["stars"]
            insertDict["enemydestructionpercentage"] = json["opponent"]["destructionPercentage"]
            insertDict["enemytag"] = json["opponent"]["tag"]

            
            if warExists:
                conn.execute(update(clanwars).where(clanwars.c.id == insertDict["id"]).values(insertDict))
                # TO DO
                # Find out if there is a new update and then text if changed
                for player in json["clan"]["members"]:
                    print(player["name"])
                    if "attacks" not in player:
                        print(f'{player["name"]} did not attack')
                    else:
                        for attack in player["attacks"]:
                            #For each attack for every player create the key
                            playerpk = f'{json["startTime"]}{player["tag"]}{attack["defenderTag"]}'
                            #Here check for existence in the database before adding vs inserting
                            result = conn.execute(select(playerwarattacks).where(playerwarattacks.c.id == playerpk)) 
                            result = result.fetchone()
                            if result is None:
                                insertDict = {}
                                insertDict["id"] = playerpk
                                insertDict["townhalllevel"] = player["townhallLevel"]
                                insertDict["mapposition"] = player["mapPosition"]
                                insertDict["tag"] = player["tag"]
                                insertDict["defendertag"] = attack["defenderTag"]
                                insertDict["stars"] = attack["stars"]
                                insertDict["destructionpercentage"] = attack["destructionPercentage"]
                                insertDict["odernum"] = attack["order"]
                                insertDict["duration"] = attack["duration"]

                                conn.execute(insert(playerwarattacks), insertDict)
                                conn.commit()

                            else:
                                print("Attack already exists in the table")

                    if "bestOpponentAttack" not in player:
                        playerpk = f'{json["startTime"]}{player["tag"]}'
                        print(f'{player["name"]} did not get attacked')

            else:
                conn.execute(insert(clanwars), insertDict)
            conn.commit()

scheduler = BlockingScheduler()
scheduler.add_job(updateHistoryTables, 'interval', seconds=900)
scheduler.add_job(warUpdates, 'interval', seconds=60)
scheduler.start()
