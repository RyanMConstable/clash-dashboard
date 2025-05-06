from fastapi import FastAPI
from pydantic import BaseModel
import requests
from sqlalchemy import Table, select, insert, MetaData, Integer, create_engine


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
    # TO DO
    # Create logic for if someone already signed up
    tags = {}
    with engine.connect() as conn:
        result = conn.execute(select(userinfo))
        for row in result:
            if row[1] not in tags:
                tags[row[1]] = 0

        if signup.tag not in tags:
            #Here we want to check the curl
            
        

    return tags

@app.get("/")
async def root():
    return {"message": "Hello World"}
