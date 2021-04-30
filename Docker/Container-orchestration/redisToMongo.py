#Alle noodzakelijke modules en bibliotheken importeren
import pandas as pd
import time
import pymongo as mongo
import json
import redis

#Connecteren met Redis
connectie = redis.Redis(host='redis', port=6379, db=0)

#Connecteren met MongoDB
client = mongo.MongoClient("mongodb://mongo:27017") #Connecteren met Mongo
database = client["highest_hashes"] #Een naam kiezen voor de database
hoogste_hashes = database["values"] #Een naam kiezen voor de data uit de database (collection)

def toMongo(connectie, hoogste_hashes):
    #Data halen uit Redis
    data1 = connectie.get('data')

    if data1 is None:
        print(data1)

    else:
        #Data inlezen als json
        data_string = data1.decode('utf-8')
        json_data = json.loads(data_string)

        #Json converteren naar dataframe    
        df = pd.DataFrame(json_data)

        #Dataframe sorteren volgens USD
        hoogste = df.sort_values(by=['USD'], ascending=False)
        #De eerste rij is de hash met de hoogste waarde in USD
        hoogste = hoogste.head(1)
        #print(hoogste)

        #Hash met de hoogste waarde in USD converteren naar json
        json_data = hoogste.to_json(orient="records").replace('[','').replace(']','')
        invoer = json.loads(json_data)
        #Hash met de hoogste waarde in USD toevoegen aan de database van MongoDB
        hoogste_hashes.insert_one(invoer)

#Elke minuut alles herhalen
while True: 
    try:
        print("Save to MongoDB")
        toMongo(connectie, hoogste_hashes)
    except:
        pass
    time.sleep(60)
