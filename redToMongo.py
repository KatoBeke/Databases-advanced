#Alle noodzakelijke modules en bibliotheken importeren
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import time
import pymongo as mongo
import json
import redis

#Connectie maken met redis
r = redis.Redis()

#MongoDB
client = mongo.MongoClient("mongodb://localhost:27017") #Connecteren met Mongo
database = client["highest_hashes"] #Een naam kiezen voor de database
hoogste_hashes = database["values"] #Een naam kiezen voor de data uit de database (collection)


data = pd.DataFrame(columns=['Hash','Time', 'BTC', 'USD'])
hashen = []
Time = []
btc = []
usd = []

def toMongo(connectie, hoogste_hashes):
    data = r.get('data')
    result = pd.read_json(data)
     #Dataframe sorteren volgens USD
    hoogste = result.sort_values(by=['USD'], ascending=True)
    #De laatste rij is de hash met de hoogste waarde in USD
    hoogste = hoogste.tail(1)

    #MongoDB
    client = mongo.MongoClient("mongodb://localhost:27017") #Connecteren met Mongo
    database = client["highest_hashes"] #Een naam kiezen voor de database
    hoogste_hashes = database["values"] #Een naam kiezen voor de data uit de database (collection)
    hoogste_hashes.insert_one(hoogste) #Data invoeren in de database van MongoDB

    
#Elke minuut alles herhalen
while True: 
    toMongo(connectie, hoogste_hashes)
    time.sleep(60)