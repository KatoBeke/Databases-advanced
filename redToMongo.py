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
    data1 = connectie.get('data')
    print(data1)
    print(type(data1),"datatype")

    #data_df = pd.DataFrame(data1,colums=['Hash'],'Time','BTC','USD'])
    #df = pd.DataFrame(data=data1)
    #print(df)
    #data = pd.DataFrame(colums=['Hash'],'Time','BTC','USD'])
    #data.append({'Hash': hashen, 'Time': Time, 'BTC': btc, 'USD': usd}, ignore_index=True)
    #result = pd.read_json(data)

    #Dataframe sorteren volgens USD
    #hoogste = result.sort_values(by=['USD'], ascending=False)
    #De eerste rij is de hash met de hoogste waarde in USD
    #hoogste = hoogste.head(1)
    #print(hoogste)

    #Hash met de hoogste waarde in USD converteren naar json
    #json_data = hoogste.to_json(orient="records").replace('[','').replace(']','')
    #invoer = json.loads(json_data)
    #Hash met de hoogste waarde in USD toevoegen aan de database van MongoDB
    #hoogste_hashes.insert_one(invoer)

    
#Elke minuut alles herhalen
while True: 
    time.sleep(60)
    toMongo(connectie, hoogste_hashes)