from fastapi import FastAPI
from pydantic import BaseModel
import requests
from sqlalchemy import Table, select, insert, MetaData, Integer, create_engine
from config import *
from urllib.parse import quote

TOK = os.getenv("TOK")

HEADERS = {"Authorization": f"Bearer {TOK}", "Content-Type": "application/json"}

engine = create_engine("postgresql://postgres:changeme@db:5432/cocdb")
metadata = MetaData()
userinfo = Table("userinfo", metadata, autoload_with=engine)

app = FastAPI()


class Signup(BaseModel):
    tag: str
    phonenumber: str
    password: str
    otp: str

@app.post("/signup/")
async def create_item(signup: Signup):
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

            if result.json()["status"] == "ok":
                conn.execute(insert(userinfo), {"playertag": signup.tag, "phonenumber": signup.phonenumber, "passwd": signup.password})
                conn.commit()
            else:
                return {"status":"invalidtoken"}
        else:
            return {"status":"exists"}
            
        
    return {"status":"ok"}

@app.get("/")
async def root():
    return {"message": "Hello World"}
