#Alle noodzakelijke modules en bibliotheken importeren
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import time
import pymongo as mongo
import json
import redis

#Connecteren met Redis
connectie = redis.Redis()

#Connecteren met MongoDB
client = mongo.MongoClient("mongodb://localhost:27017") #Connecteren met Mongo
database = client["highest_hashes"] #Een naam kiezen voor de database
hoogste_hashes = database["values"] #Een naam kiezen voor de data uit de database (collection)


data = pd.DataFrame(columns=['Hash','Time', 'BTC', 'USD'])
hashen = []
Time = []
btc = []
usd = []

def toMongo(connectie, hoogste_hashes):
    data = connectie.get('data')
    result = pd.read_json(data)
    #Dataframe sorteren volgens USD
    hoogste = result.sort_values(by=['USD'], ascending=True)
    #De laatste rij is de hash met de hoogste waarde in USD
    hoogste = hoogste.tail(1)

    #Hash met de hoogste waarde in USD toevoegen aan de database van MongoDB
    hoogste_hashes.insert_one(hoogste)

    
#Elke minuut alles herhalen
while True: 
    toMongo(connectie, hoogste_hashes)
    time.sleep(60)