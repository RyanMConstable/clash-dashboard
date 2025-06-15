from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import requests
from sqlalchemy import Table, select, insert, MetaData, Integer, create_engine, and_, func
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import quote
import os

TOK = os.getenv("TOK")

HEADERS = {"Authorization": f"Bearer {TOK}", "Content-Type": "application/json"}

engine = create_engine("postgresql://postgres:changeme@db:5432/cocdb")
metadata = MetaData()

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://clash-frontend"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)

class Signup(BaseModel):
    tag: str
    phonenumber: str
    password: str
    otp: str

class Login(BaseModel):
    user: str
    password: str

@app.post("/api/signup")
async def create_item(signup: Signup):
    userinfo = Table("userinfo", metadata, autoload_with=engine)

    print(signup.tag, signup.phonenumber, signup.password, signup.otp)
    tags = {}
    with engine.connect() as conn:
        result = conn.execute(select(userinfo))
        for row in result:
            if row[1] not in tags:
                tags[row[1]] = 0

        if signup.tag not in tags:
            encodedTag = quote(signup.tag)

            payload = {"token": signup.otp}
            url = f'https://api.clashofclans.com/v1/players/{encodedTag}/verifytoken'

            result = requests.post(url, headers=HEADERS, json=payload)
            if result.status_code == 500:
                return {"status":"incorrectplayertag"}

            print(result.json())
            if result.json()["status"] == "ok":
                conn.execute(insert(userinfo), {"playertag": signup.tag, "phonenumber": signup.phonenumber, "passwd": signup.password})
                conn.commit()
            else:
                return {"status":"invalidtoken"}
        else:
            return {"status":"exists"}
            
        
    return {"status":"ok"}

@app.post("/api/login")
async def create_item(login: Login):
    userinfo = Table("userinfo", metadata, autoload_with=engine)
    playerhistory = Table("playerhistory", metadata, autoload_with=engine)

    with engine.connect() as conn:
        result = conn.execute(select(userinfo).where(and_(
            userinfo.c.playertag == login.user,
            userinfo.c.passwd == login.password
            )
                            )
                              ).fetchone()
        print(f'Userinfo: {result}')
        if result is None:
            return {"status": "invalid"}

        result = conn.execute(select(playerhistory).where(
            playerhistory.c.playertag == login.user
            )
                              ).fetchone()

        print(f'Playerhistory: {result}')

    return {"status": "ok", "clantag": result[-1][1:]}

@app.get("/api/clandashboard")
async def get_clan_dashboard(
        clantag: str = Query(..., description="Clan tag to fetch data")
        numattacks: Optional[int] = Query(None, description="Create total elo from specified number of attacks")
        ):

    fulltag = '#' + clantag
    
    clanwars = Table("clanwars", metadata, autoload_with=engine)
    clanlist = Table("clanlist", metadata, autoload_with=engine)
    
    with engine.connect() as conn:
        #CURRENT WAR INFO
        stmt = select(clanwars).where(
                func.split_part(clanwars.c.id, '#', 2) == clantag
                ).order_by(clanwars.c.id.desc())
        result = conn.execute(stmt).mappings().fetchone()

        clanname = conn.execute(select(clanlist).where(
                clanlist.c.clantag == fulltag
                )).fetchone()

        #PLAYER ELO INFO


    return {"status": "ok", "clanvalues": result, "clanname": clanname[1]}
