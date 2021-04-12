#Alle noodzakelijke modules en bibliotheken importeren
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas 
import time
import os

url = "https://www.blockchain.com/btc/unconfirmed-transactions"
request = Request(url) #verzoek krijgen
answer = urlopen(request) #het antwoord opvangen
html = answer.read() #het antwoord lezen

#HTML-parser creëren om gegegevens uit HTML te halen
page = BeautifulSoup(html, "html.parser")
blockchain = page.find_all("div",{"class":"sc-1g6z4xm-0 hXyplo"})

#Lijsten maken van de hash, tijd, btc en usd voor elke bitcoin transactie
hashed = []
timed = []
btc =  []
usd = []

usds = []
resultaat = []
result = []

maximumUSD = 0

#Functie om hash, tijd, btc en usd van de url te krijgen
def getTransactions(hashed,timed,btc,usd):
    for item in blockchain:
        Hash = item.find_all("a", {"class": "sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk d53qjk-0 ctEFcK"})[0].text
        print(Hash)
        time = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[0].text
        print(time)
        BTC = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[1].text
        print(BTC)
        USD = item.find_all("span", {"class": "sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"})[2].text
        print(USD)
        #alle bedragen in USD in een lijst steken
        usds.append(USD)

        #alle hash, tijd, btc en usd in 1 lijst steken
        result.append(Hash)
        result.append(time)
        result.append(BTC)
        result.append(USD)

resultaat.append(getTransactions(hashed,timed,btc,usd))

#Het hoogste bedrag in USD vinden
maximumUSD = max(usds)
usd.append(maximumUSD)

#Lijsten maken van de hash, tijd, btc en usd van de meest waardevolle Hash voor Bitcoin per minuut in USD
dollar = []
bitcoin = []
tijd = []
hashen = []

#Kijken wat het maximum bedrag in USD als index heeft in de grote result lijst en dit bedrag toevoegen aan dollar-lijst
indexMaxUSD = result.index(maximumUSD)
maxiUSD = result[indexMaxUSD]
dollar.append(maxiUSD)

#Kijken  wat het overeenkomstige bedrag in BTC heeft als index heeft in de grote result lijst en dit bedrag toevoegen aan bitcoin-lijst
indexBTC = indexMaxUSD - 1
btcs = result[indexBTC]
bitcoin.append(btcs)

#Kijken  wat de overeenkomstige tijd als index heeft in de grote result lijst en deze tijd toevoegen aan tijd-lijst
indexTime = indexMaxUSD - 2
times = result[indexTime]
tijd.append(times)

#Kijken  wat de overeenkomstige hash als index heeft in de grote result lijst en deze hash toevoegen aan hashen-lijst
indexHash = indexMaxUSD - 3
hashes = result[indexHash]
hashen.append(hashes)

#De hash, tijd, btc en usd van de meest waardevolle Hash voor Bitcoin per minuut in USD in dataframe zetten en toevoegen aan een bestand
data = {'Hash':hashen,'Time':tijd,'BTC':bitcoin,'USD':dollar}
dataframe = pandas.DataFrame(data)
dataframe.head(1).to_csv('result.log', header = True, index = None, sep = ' ' , mode = 'a')

#Elke minuut alles herhalen
while True: 
    time.sleep(60)
    os.system("scraper.py")
  
  


    