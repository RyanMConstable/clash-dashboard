import requests
from urllib.parse import quote
from config import *
from sqlalchemy import Table, Column, MetaData, Integer, Computed, event, create_engine, select, insert
from datetime import datetime, timezone

now = datetime.now()

engine = create_engine("postgresql://postgres:changeme@localhost:5432/cocdb")
metadata = MetaData()
userinfo = Table("userinfo", metadata, autoload_with=engine)

users = {}

with engine.connect() as conn:
    result = conn.execute(select(userinfo))
    for row in result:
        if row[1] not in users:
            users[row[1]] = row[2]

#users is in the format {PLAYERTAG: PHONENUMBER}
playerhistory = Table("playerhistory", metadata, autoload_with=engine)
with engine.connect() as conn:
    for user in users:
        encodedUser = quote(user)
        url = f"https://api.clashofclans.com/v1/players/{encodedUser}"
        result = requests.get(url, headers=HEADERS)
        if result.status_code != 200:
            print(f"[ERROR]: Status code: {result.status_code}")
            continue
        clantag = result.json()['clan']['tag']

        insertDict = {}
        #Here is where we take the json and set up the insert dictionary
        insertDict['time'] = now
        insertDict['playertag'] = user
        insertDict['townhalllevel'] =
        insertDict['townhallweaponlevel'] =
        insertDict['explevel'] =
        insertDict['trophies'] =
        insertDict['besttrophies'] =
        insertDict['warstars'] =
        insertDict['attackwins'] =
        insertDict['defensewins'] =
        insertDict['builderhalllevel'] =
        insertDict['builderbasetrophies'] =
        insertDict['bestbuilderbasetrophies'] =
        insertDict['role'] =
        insertDict['warpreference'] =
        insertDict['donations'] =
        insertDict['donationsreceived'] =
        insertDict['clancapitalcontributions'] =
        insertDict['league'] =
        insertDict['builderleague'] =
        insertDict['clantag'] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =
        insertDict[''] =

        conn.execute(insert(playerhistory), insertDict)
        conn.commit()
