import requests
import urllib.parse
from config import *

encodedPlayerTag = urllib.parse.quote(playerTag)
encodedClanTag = urllib.parse.quote(clanTag)

#This gets the player information into a json format
url = f'https://api.clashofclans.com/v1/players/{encodedPlayerTag}'
player = requests.get(url, headers=HEADERS).json()

#This gets the current clanwar information
url = f'https://api.clashofclans.com/v1/clans/{encodedClanTag}/currentwar'
clan = requests.get(url, headers=HEADERS).json()
state = clan["state"]

#print(player)
print(clan)

#If we're checking daily we can grab this and add it to the database
if state == "inWar" or state == "warEnded":
    uniqueIndex = f"{clan['clan']['tag']}{clan['startTime'].split('T')[0]}"
    if state == "warEnded":
        print("Add each player attack to a table with player tag and clan tag")
    else:
        print("Monitor for updates, check against current info and update db in real time")
