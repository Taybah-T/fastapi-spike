import datetime
import os
import psycopg
from peewee import *
from dotenv import load_dotenv
from fastapi import FastAPI,Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

load_dotenv()

connection = psycopg.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT", "5432")
)

class BaseModel(Model):
    class Meta:
        database = connection
        
class Coin(BaseModel):
    coin_id = IntegerField(primary_key=True)
    coin_name = TextField()
    
class Duties(BaseModel):
    duty_id = IntegerField(primary_key=True)
    duty_name = TextField()
    duty_descrpition = TextField()
    
connection.connect()
connection.create_tables([Coin, Duties])