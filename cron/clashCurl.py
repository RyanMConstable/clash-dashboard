import requests
from urllib.parse import quote
from config import *
from sqlalchemy import Table, Column, MetaData, Integer, Computed, event, create_engine, select, insert
from datetime import datetime, timezone

now = datetime.now()

engine = create_engine("postgresql://postgres:changeme@localhost:5432/cocdb")
metadata = MetaData()
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
        insertDict['townhallweaponlevel'] = json['townHallWeaponLevel']
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
            conn.execute(insert(clanlist), {'clantag':f'{clan}'})
            conn.commit()
