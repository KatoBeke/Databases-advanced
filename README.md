# Databases-advanced
Deze repository is onderdeel van een opdracht voor het vak Databases Advanced. Tijdens deze opdrachten leerden we werken met MongoDB, Redis, Docker, Ubuntu, ... Om deze opdracht overzichtelijk te houden werd de opdracht opgesplitst in meerdere kleine opdrachten.
## Opdracht 1: Scraper (scraper.py)
Ik heb de volgende website gebruikt om te scrapen: https://www.blockchain.com/btc/unconfirmed-transactions <br>
Ik heb hiervan de hash, time, btc en usd gescrapet. Daarna heb ik de hash, time, btc en usd van de meest waardevolle Hash voor Bitcoin per minuut in USD gezocht en dit in een dataframe gezet. Tenslotte heb ik dit dan toegevoegd aan result.log.

### Ubuntu
Het doel van deze opdracht is om de scraper te runnen op Ubuntu Virtual Machine. 
Ik heb mijn script op mijn Windows pc gemaakt. Download deze repository op Ubuntu via de commando git clone met de link https://github.com/KatoBeke/Databases-advanced.git. <br> 

Om het script **scraper.py** te kunnen gebruiken moet je python runnen. Ik raad je de laatste versie van Python (3.9.2) aan. Om python te installeren gebruik je de commando sudo apt install python3. <br>
Daarnaast moet je ook pip, pandas en bs4 installeren. Je kan dit doen door de volgende commando's te typen in je Python terminal:
* sudo apt install python3-pip
* pip3 install pandas
* pip3 install bs4 

Het is ook heel belangrijk dat als je het script **scraper.py** wil runnen je in dezelfde map zit als waar **scraper.py** staat. Om naar dezelfde map te gaan typ je cd Databases-advanced. <br> <br>
Om het script **scraper.py** te kunnen runnen gebruik je de commando python3 scraper.py. Om de uitvoering van het script te stoppen, typ je ctrl + c in de terminal.

## Opdracht 2: Mongo (mongo.py, bash.sh en mongo.sh)
Het doel van deze opdracht is de data uit de vorige opdracht in MongoDB plaatsen. 

### Ubuntu
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando git pull met de link https://github.com/KatoBeke/Databases-advanced.git. <br> 
#### MongoDB
Om **MongoDB** te installeren moet je de volgende commando's gebruiken (of gebruik **bash.sh** van de map Bash scripts):
* sudo apt install curl
* curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
* echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
* sudo apt update
* sudo apt install mongodb-org

Om **MongoDB** te starten gebruik je de commando's (of gebruik **mongo.sh** van de map Bash scripts):
* sudo systemctl start mongod
* sudo systemctl status mongod
* sudo systemctl enable mongod
* mongo --eval 'db.runCommand({ connectionStatus: 1 })'

Ik heb mijn scraper aangepast en dit een nieuwe naam gegeven namelijk **mongo.py**. <br>
Om **mongo.py** te kunnen gebruiken en dus mongo te runnen, moet je de volgende commando's gebruiken:
* pip3 install pymongo 
* cd < mongodb installation dir >/ bin
* mongo

Het is ook heel belangrijk dat als je het script **mongo.py** wil runnen je in dezelfde map zit als waar **mongo.py** staat. Om naar dezelfde map te gaan typ je cd Databases-advanced. <br> <br>
Om het script **mongo.py** te kunnen runnen gebruik je de commando python3 mongo.py. Om de uitvoering van het script te stoppen, typ je ctrl + c in de terminal.

#### MongoDB Compass
Als u een visuele interface wilt, kunt u MongoDB Compass installeren. Hiervoor gebruik je de volgende commando's: 
* apt-get update
* wget https://dowloads.mongodb.com/compass/mongodb-compass_1.26.1_amd64.deb
* sudo dpkg -i mongodb-compass_1.26.1_amd64.deb

Ga nu naar applications op Ubuntu en selecteer MongoDB Compass. MongoDB Compass wordt geopend. 
Om te connecteren klik je op Connect en Connect to... Je kan op 2 manieren connecteren:
* door een connectie string te plakken in de balk die er verschijnt en dan op Connect te drukken of
* klik op Fill in connection fields individually. Er verschijnt een scherm waar je hostname en port kan invullen. Vul bij hostname localhost en bij port 27017 in. Vink SRV record af en zet authentication op None. Druk op Connect.

Nu krijg je een overzicht van alle databases. Zodra je op een database klikt krijg je een scherm met de collections van die database. Druk op de database highest_hashes op de collection values. 
Zodra je het script **mongo.py** begint te runnen wordt elke minuut de meest waardevolle Hash voor Bitcoin per minuut in USD aan deze database en collection toegevoegd. Het ziet er als volgt uit:
![image](https://user-images.githubusercontent.com/74418649/114557525-0cca8f00-9c6a-11eb-9eb4-9b70f092727d.png)

## Opdracht 3: Redis (red.py, redisToMongo.py en redis.sh)
Het doel van deze opdracht is om de data die ik heb gescrapet (scraper.py) onmiddellijk te bewaren in een Redis-database (**red.py**). Deze Redis-database houdt deze data slechts 1 minuut bij (**red.py**). Als de data zich in mijn Redis-databank bevindt, haalt mijn **redisToMongo.py** de data uit de Redis-databank en filtert de data zodat enkel de hash met de hoogste waarde in USD overblijft. Vervolgens wordt de hash met de hoogste waarde in USD definitief opgeslagen in een database van MongoDB. Als de data is opgeslagen in de MongoDB-database wordt de data uit de Redis-database verwijderd. Heel dit proces gebeurt om de 1 minuut.

### Ubuntu
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando git pull met de link https://github.com/KatoBeke/Databases-advanced.git. <br> 

#### Redis
Om **Redis** te installeren moet je de volgende commando's gebruiken (of gebruik **redis.sh** van de map Bash scripts):
* sudo apt-get install redis-server
* sudo systemctl status redis-server

Om **Redis** te starten gebruik je het commando _sudo systemctl start redis_ (of gebruik **redis.sh** van de map Bash scripts).

Om **Redis** te stoppen gebruik je het commando _sudo systemctl stop redis_ (of gebruik **redis.sh** van de map Bash scripts).

Voor deze opdracht heb ik 2 Python scripts namelijk **red.py** en **redisToMongo.py**. Gebruik het script **red.py** om de gescrapete data in te voeren in de Redis-databank. Gebruik het script **redisToMongo.py** om uit de Redis-databank de hash met de hoogste waarde in USD per minuut te halen en in te voeren in de MongoDB database. <br>
Om **red.py** en **redisToMongo.py** te kunnen gebruiken en dus mongo te runnen, moet je de volgende commando's gebruiken:
* pip3 install redis 

Het is ook heel belangrijk dat als je de script **red.py** en **redisToMongo.py** wil runnen je in dezelfde map zit als waar **red.py** en **redisToMongo.py** staan. Om naar dezelfde map te gaan typ je cd Databases-advanced. <br> <br>
Om de scripts **red.py** en **redisToMongo.py** te kunnen runnen gebruik je de commando's python3 red.py en python3 redisToMongo.py. Om de uitvoering van de scripts te stoppen, typ je ctrl + c in de terminal.

#### MongoDB Compass
Als u een visuele interface wilt, kunt u MongoDB Compass installeren. Zie Opdracht 2!!!

## Opdracht 4: Docker Images
Het doel van deze opdracht is het project omzetten in containers. Op deze manier kan je elk onderdeel in een docker container runnen. Hierdoor kan je dit project overal draaien waar je ook maar wilt. 
Het doel van deze opdracht is de bestaande containers van mongo en redis runnen op Ubuntu. Hiervoor moet je een account aanmaken via https://hub.docker.com/.

### Ubuntu
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando git pull met de link https://github.com/KatoBeke/Databases-advanced.git. <br> 

#### Docker
Als je Windows of MacOS gebruikt moet je via https://www.docker.com/products/docker-desktop Docker installeren.
Als je Linux hebt moet ik je in je Ubuntu terminal het volgende ingeven: sudo apt install docker.io.
Je moet ook sowieso een account aanmaken via https://hub.docker.com/. 

##### MongoDB & Redis
Om de containers van mongo en redis te runnen op Ubuntu ga je naar de volgende sites:
* https://hub.docker.com/_/mongo (commando docker pull mongo)
* https://hub.docker.com/_/redis (commando docker pull redis)

## Opdracht 5: Container Orchestration
Het doel van deze opdracht is het project omzetten in containers. Op deze manier kan je elk onderdeel in een docker container runnen. Hierdoor kan je dit project overal draaien waar je ook maar wilt. 
Het doel van deze opdracht van deze opdracht was zelf nieuwe containers maken voor de scraper en filter. Hiervoor moet je een account aanmaken via https://hub.docker.com/.
Je kan zelf ook je eigen images maken met Dockerfiles of je kan mijn gemaakte images van mijn docker hub profiel halen.

### Ubuntu
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando git pull met de link https://github.com/KatoBeke/Databases-advanced.git. <br> 

#### Docker
Als je Windows of MacOS gebruikt moet je via https://www.docker.com/products/docker-desktop Docker installeren.
Als je Linux hebt moet ik je in je Ubuntu terminal het volgende ingeven: sudo apt install docker.io.
Je moet ook sowieso een account aanmaken via https://hub.docker.com/. 

##### Creër je eigen images
Maak een Dockerfile met de volgende code en geen extensie. Je kan natuurlijk ook mijn dockerfiles downloaden van mijn Github repository.
###### Scraper

###### Parser

###### MongoDB & Redis
Om de containers van mongo en redis te runnen op Ubuntu ga je naar de volgende sites:
* https://hub.docker.com/_/mongo (commando docker pull mongo)
* https://hub.docker.com/_/redis (commando docker pull redis)

##### Images pullen
Ga naar ...

##### Images veranderen naar containers

### Network creëren en containers toevoegen
