# Databases-advanced
# Opdracht 1: Scraper (scraper.py)
Ik heb de volgende website gebruikt om te scrapen: https://www.blockchain.com/btc/unconfirmed-transactions <br>
Ik heb hiervan de hash, time, btc en usd gescrapet. Daarna heb ik de hash, time, btc en usd van de meest waardevolle Hash voor Bitcoin per minuut in USD gezocht en dit in een dataframe gezet. Tenslotte heb ik dit dan toegevoegd aan result.log.

## Ubuntu
Het doel van deze opdracht is om de scraper te runnen op Ubuntu Virtual Machine. 
Ik heb mijn script op mijn Windows pc gemaakt. Daarna heb ik deze repository gedownload op Ubuntu via de commando git clone met de link https://github.com/KatoBeke/Databases-advanced.git. <br> 

Om het script scraper.py te kunnen gebruiken moet je python runnen. Ik raad je de laatste versie van Python (3.9.2) aan. Om python te installeren gebruik je de commando sudo apt install python3. <br>
Daarnaast moet je ook pip, pandas en bs4 installeren. Je kan dit doen door de volgende dingen te typen in je Python terminal:
* sudo apt install python3-pip
* pip3 install pandas
* pip3 install bs4 

Het is ook heel belangrijk dat als je het script scraper.py wil runnen je in dezelfde map zit als waar scraper.py staat. Om naar dezelfde map te gaan typ je sudo su. Typ nu cd gevolgd door de naam van je repository in Github (bij mij is dit dan cd Databases-advanced). 

Om het script scraper.py te kunnen runnen gebruik je de commando python3 scraper.py. Om de uitvoering van het script te stoppen, typ je ctrl + c. in de terminal.

# Opdracht 2: Mongo (mongo.py en mongo.sh)
Het doel van deze opdracht is de data uit de vorige opdracht in MongoDB plaatsen. 

## Ubuntu
### MongoDB
Ik heb mijn scraper aangepast en dit een nieuwe naam gegeven namelijk mongo.py. 

# Opdracht 3: Redis

# Opdracht 4: Docker Images

# Opdracht 5: Container Orchestration
