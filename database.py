from peewee import *
import os 
from peewee import PostgresqlDatabase
from dotenv import load_dotenv
from fastapi import FastAPI,Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

load_dotenv()

db = PostgresqlDatabase(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT", "5432")
)

class BaseModel(Model):
    class Meta:
        database = db

class Coin(BaseModel):
    coin_id = IntegerField(primary_key=True)
    coin_name = TextField()

class Duty(BaseModel):
    duty_id = IntegerField(primary_key=True)
    duty_name = TextField()
    duty_description = TextField()

db.connect()
db.create_tables([Coin, Duty])