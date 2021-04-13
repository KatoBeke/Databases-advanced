#Alle noodzakelijke modules en bibliotheken importeren
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import time

#Functie maken voor alle rijen met hash, tijd, btc en usd uit url te halen
def getBlockchain():
    url = "https://www.blockchain.com/btc/unconfirmed-transactions"
    request = Request(url) #verzoek krijgen
    answer = urlopen(request) #het antwoord opvangen
    html = answer.read() #het antwoord lezen

    #HTML-parser creëren om gegegevens uit HTML te halen
    page = BeautifulSoup(html, "html.parser")
    blockchain = page.find_all("div",{"class":"sc-1g6z4xm-0 hXyplo"})

    return blockchain

#Lijst maken van de hash, tijd, btc en usd voor elke bitcoin transactie
result = []

#Functie om hash, tijd, btc en usd van de url te krijgen
def getTransactions():
    blockchain = getBlockchain()
    data = pd.DataFrame(columns=['Hash','Time', 'BTC', 'USD']) #Dataframe aanmaken en kolommen een naam geven
    for item in blockchain:
        Hash = item.find_all("a", {"class": "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})[0].text

        time = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[0].text

        BTC = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[1].text

        USD = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[2].text
        USD = USD.replace(',','')

        #Alle hash, time, btc en usd in 1 lijst steken en zorgen dat lijst telkens leeg is nadien
        result.clear()
        result.append(Hash)
        result.append(time)
        result.append(BTC)
        result.append(USD)

        #De hash, time, btc en usd uit lijst halen en telkens toevoegen aan dataframe
        hashen = result[0]
        Time = result[1]
        btc = result[2]
        usd = result[3]

        data = data.append({'Hash': hashen, 'Time': Time, 'BTC': btc, 'USD': usd}, ignore_index=True)
        #Dataframe sorteren volgens USD
        highest_usd = data.sort_values(by=['USD'], ascending=True)
        #De laatste rij is de hash met de hoogste waarde in USD
        highest_usd = highest_usd.tail(1)
    #De hash met de hoogste waarde in USD toevoegen aan result.log
    highest_usd.to_csv('result.log', header = True, index = None, sep = ' ' , mode = 'a')
        
#Elke minuut alles herhalen
while True: 
    time.sleep(60)
    getTransactions()
    