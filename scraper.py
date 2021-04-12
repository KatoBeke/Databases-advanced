#Alle noodzakelijke modules en bibliotheken importeren
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import time

def getBlockchain():
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    request = Request(url) #verzoek krijgen
    answer = urlopen(request) #het antwoord opvangen
    html = answer.read() #het antwoord lezen

    #HTML-parser creëren om gegegevens uit HTML te halen
    page = BeautifulSoup(html, "html.parser")
    blockchain = page.find_all("div",{"class":"sc-1g6z4xm-0 hXyplo"})

    return blockchain

#Lijsten maken van de hash, tijd, btc en usd voor elke bitcoin transactie
hashed = []
timed = []
btc =  []
usd = []

result = []

#Functie om hash, tijd, btc en usd van de url te krijgen
def getTransactions(hashed,timed,btc,usd):
    blockchain = getBlockchain()
    data = pd.DataFrame(columns=['Hash','Time', 'BTC', 'USD'])
    for item in blockchain:
        Hash = item.find_all("a", {"class": "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})[0].text

        time = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[0].text

        BTC = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[1].text

        USD = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[2].text
        USD = USD.replace(',','')

        #alle hash, tijd, btc en usd in 1 lijst steken
        result.clear()
        result.append(Hash)
        result.append(time)
        result.append(BTC)
        result.append(USD)

        data = data.append({'Hash': result[0], 'Time': result[1], 'BTC': result[2], 'USD': result[3]}, ignore_index=True)
        highest_usd = data.sort_values(by=['USD'], ascending=True)
        highest_usd = highest_usd.tail(1)
    highest_usd.to_csv('result.log', header = True, index = None, sep = ' ' , mode = 'a')
        
#Elke minuut alles herhalen
while True: 
    getTransactions(hashed,timed,btc,usd)
    time.sleep(60)