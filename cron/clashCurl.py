import requests
from urllib.parse import quote
from config import *
from sqlalchemy import Table, Column, MetaData, Integer, Computed, event, create_engine, select


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
for user in users:
    encodedUser = quote(user)
    url = f"https://api.clashofclans.com/v1/players/{encodedUser}"
    result = requests.get(url, headers=HEADERS)
    print(result.json())
