# Databases-advanced
Deze repository is onderdeel van een opdracht voor het vak Databases Advanced. Tijdens deze opdrachten leerden we werken met MongoDB, Redis, Docker, Ubuntu, ... Om deze opdracht overzichtelijk te houden werd de opdracht opgesplitst in meerdere kleine opdrachten.
## Opdracht 1: Scraper (scraper.py)
Ik heb de volgende website gebruikt om te scrapen: https://www.blockchain.com/btc/unconfirmed-transactions <br>
Ik heb hiervan de hash, time, btc en usd gescrapet. Daarna heb ik de hash, time, btc en usd van de meest waardevolle Hash voor Bitcoin per minuut in USD gezocht en dit in een dataframe gezet. Tenslotte heb ik dit dan toegevoegd aan result.log.

### Ubuntu
Het doel van deze opdracht is om de scraper te runnen op Ubuntu Virtual Machine. 
Ik heb mijn script op mijn Windows pc gemaakt. Download deze repository op Ubuntu via de commando <code>git clone https://github.com/KatoBeke/Databases-advanced.git</code>. <br> 

Om het script **scraper.py** te kunnen gebruiken moet je python runnen. Ik raad je de laatste versie van Python (3.9.2) aan. Om python te installeren gebruik je de commando <code>sudo apt install python3</code>. <br>
Daarnaast moet je ook pip, pandas en bs4 installeren. Je kan dit doen door de volgende commando's te typen in je Python terminal: <br>
<code>sudo apt install python3-pip</code> <br>
<code>pip3 install pandas</code> <br>
<code>pip3 install bs4</code>

Het is ook heel belangrijk dat als je het script **scraper.py** wil runnen je in dezelfde map zit als waar **scraper.py** staat. Om naar dezelfde map te gaan typ je <code>cd Databases-advanced</code>. <br> <br>
Om het script **scraper.py** te kunnen runnen gebruik je de commando <code>python3 scraper.py</code>. Om de uitvoering van het script te stoppen, typ je ctrl + c in de terminal.

## Opdracht 2: Mongo (mongo.py, bash.sh en mongo.sh)
Het doel van deze opdracht is de data uit de vorige opdracht in MongoDB plaatsen. 

### Ubuntu
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando <code>git pull https://github.com/KatoBeke/Databases-advanced.git</code>. <br> 
#### MongoDB
Om **MongoDB** te installeren moet je de volgende commando's gebruiken (of gebruik **bash.sh** van de map Bash scripts): <br>
<code>sudo apt install curl</code> <br>
<code>curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -</code> <br>
<code>echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list</code> <br>
<code>sudo apt update</code> <br>
<code>sudo apt install mongodb-org</code>

Om **MongoDB** te starten gebruik je de commando's (of gebruik **mongo.sh** van de map Bash scripts): <br>
<code>sudo systemctl start mongod</code> <br>
<code>sudo systemctl status mongod</code> <br>
<code>sudo systemctl enable mongod</code> <br>
<code>mongo --eval 'db.runCommand({ connectionStatus: 1 })'</code>

Ik heb mijn scraper aangepast en dit een nieuwe naam gegeven namelijk **mongo.py**. <br>
Om **mongo.py** te kunnen gebruiken en dus mongo te runnen, moet je de volgende commando's gebruiken: <br>
<code>pip3 install pymongo</code> <br>
<code>cd < mongodb installation dir >/ bin</code> <br>
<code>mongo</code>

Het is ook heel belangrijk dat als je het script **mongo.py** wil runnen je in dezelfde map zit als waar **mongo.py** staat. Om naar dezelfde map te gaan typ je <code>cd Databases-advanced</code>. <br> <br>
Om het script **mongo.py** te kunnen runnen gebruik je de commando <code>python3 mongo.py</code>. Om de uitvoering van het script te stoppen, typ je ctrl + c in de terminal.

#### MongoDB Compass
Als u een visuele interface wilt, kunt u MongoDB Compass installeren. Hiervoor gebruik je de volgende commando's: <br>
<code>apt-get update</code> <br>
<code>wget https://dowloads.mongodb.com/compass/mongodb-compass_1.26.1_amd64.deb</code> <br>
<code>sudo dpkg -i mongodb-compass_1.26.1_amd64.deb</code>

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
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando <code>git pull https://github.com/KatoBeke/Databases-advanced.git.</code> <br> 

#### Redis
Om **Redis** te installeren moet je de volgende commando's gebruiken (of gebruik **redis.sh** van de map Bash scripts): <br>
<code>sudo apt-get install redis-server</code> <br>
<code>sudo systemctl status redis-server</code>

Om **Redis** te starten gebruik je het commando <code>sudo systemctl start redis</code> (of gebruik **redis.sh** van de map Bash scripts).

Om **Redis** te stoppen gebruik je het commando <code>sudo systemctl stop redis</code> (of gebruik **redis.sh** van de map Bash scripts).

Voor deze opdracht heb ik 2 Python scripts namelijk **red.py** en **redisToMongo.py**. Gebruik het script **red.py** om de gescrapete data in te voeren in de Redis-databank. Gebruik het script **redisToMongo.py** om uit de Redis-databank de hash met de hoogste waarde in USD per minuut te halen en in te voeren in de MongoDB database. <br>
Om **red.py** en **redisToMongo.py** te kunnen gebruiken en dus mongo te runnen, moet je de volgende commando's gebruiken: <br> 
<code>pip3 install redis</code> 

Het is ook heel belangrijk dat als je de script **red.py** en **redisToMongo.py** wil runnen je in dezelfde map zit als waar **red.py** en **redisToMongo.py** staan. Om naar dezelfde map te gaan typ je <code>cd Databases-advanced</code>. <br> <br>
Om de scripts **red.py** en **redisToMongo.py** te kunnen runnen gebruik je de commando's <code>python3 red.py</code> en <code>python3 redisToMongo.py</code>. Om de uitvoering van de scripts te stoppen, typ je ctrl + c in de terminal.

#### MongoDB Compass
Als u een visuele interface wilt, kunt u MongoDB Compass installeren. Zie Opdracht 2!!!

## Opdracht 4: Docker Images (Images Mongo & Redis)
Het doel van deze opdracht is het project omzetten in containers. Op deze manier kan je elk onderdeel in een docker container runnen. Hierdoor kan je dit project overal draaien waar je ook maar wilt. 
Het doel van deze opdracht is de bestaande containers van mongo en redis runnen op Ubuntu. Hiervoor moet je een account aanmaken via https://hub.docker.com/.

### Ubuntu
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando <code>git pull https://github.com/KatoBeke/Databases-advanced.git.</code> <br> 

#### Docker
Gebruik het commando <code>sudo apt install docker.io</code> in Ubuntu om Docker te installeren.
Je moet ook sowieso een account aanmaken via https://hub.docker.com/. 

##### Images Mongo & Redis
Om de images van mongo en redis te runnen op Ubuntu ga je naar de volgende sites:
* https://hub.docker.com/_/mongo (commando <code>docker pull mongo</code>)
* https://hub.docker.com/_/redis (commando <code>docker pull redis</code>)

##### Images Mongo & Redis converteren naar containers
Om de images van mongo en redis te veranderen naar containers gebruik je de volgende commando's: <br>
<code>docker run -d -p 27017:27017 mongo</code> <br>
<code>docker run -d redis</code>

Voor alle commando's te zien die je nodig hebt, ga naar de map Docker, Docker images!

##### Runnen van red.py en redisToMongo.py
Zorg dat je in de juiste map zit om te scraper te kunnen runnen: <code>cd Databases advanced</code>. <br>
Voor deze opdracht heb ik 2 Python scripts namelijk **red.py** en **redisToMongo.py**. Gebruik het script **red.py** om de gescrapete data in te voeren in de Redis-databank. Gebruik het script **redisToMongo.py** om uit de Redis-databank de hash met de hoogste waarde in USD per minuut te halen en in te voeren in de MongoDB database. <br>
Om de scripts **red.py** en **redisToMongo.py** te kunnen runnen gebruik je de commando's <code>python3 red.py</code> en <code>python3 redisToMongo.py</code>. Om de uitvoering van de scripts te stoppen, typ je ctrl + c in de terminal.

## Opdracht 5: Container Orchestration (red.py, redisToMongo.py)
Het doel van deze opdracht is het project omzetten in containers. Op deze manier kan je elk onderdeel in een docker container runnen. Hierdoor kan je dit project overal draaien waar je ook maar wilt. 
Het doel van deze opdracht was zelf nieuwe containers maken voor de scraper en filter. Hiervoor moet je een account aanmaken via https://hub.docker.com/.
Je kan zelf ook je eigen images maken met Dockerfiles of je kan mijn gemaakte images van mijn docker hub profiel halen.
Ik heb ook mijn **red.py** en **redisToMongo.py** een beetje aangepast (zie map Docker, Container Orchestration).

### Ubuntu
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando <code>git pull https://github.com/KatoBeke/Databases-advanced.git.</code> <br> 

#### Docker
Gebruik het commando <code>sudo apt install docker.io</code> in Ubuntu om Docker te installeren.
Je moet ook sowieso een account aanmaken via https://hub.docker.com/. 

##### Creër je eigen images
Downloadt mijn dockerfiles van mijn Github repository (map Docker, Container Orchestration, Docker files)! <br>
Voor meer info: https://docs.docker.com/compose/gettingstarted/ en https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/ <br>

Om Docker images te maken met de dockerfiles ga naar de map waar de dockerfiles staan (Databases-advanced/Docker/Container-orchestration/Docker-files/Scraper en Databases-advanced/Docker/Container-orchestration/Docker-files/Parser). Typ vervolgens in de terminal <code>docker build -t scraper .</code> en <code>docker build -t parser .</code>.

Om je images naar Docker Hub te pushen gebruik je de commando's: <br>
<code>docker tag scraper katobeke/databases-advanced-scraper:latest</code> <br>
<code>docker push katobeke/databases-advanced-scraper:latest</code>  <br>
<code>docker tag parser katobeke/databases-advanced-parser:latest</code> <br>
<code>docker push katobeke/databases-advanced-parser:latest</code>

##### Images pullen
Ga naar https://hub.docker.com/repository/docker/katobeke/databases-advanced-scraper en https://hub.docker.com/repository/docker/katobeke/databases-advanced-parser. <br>
Gebruik de commando's: <br>
<code>docker pull katobeke/databases-advanced-scraper:latest</code> <br>
<code>docker pull katobeke/databases-advanced-parser:latest</code>

##### Alle images opsommen
Om een overzicht te krijgen van de images gebruik je het commando: <code>docker images</code>.

##### Images verwijderen
<code>docker rmi katobeke/databases-advanced-scraper</code> <br>
<code>docker rmi katobeke/databases-advanced-parser</code>

##### Images veranderen naar containers
<code>docker run katobeke/databases-advanced-scraper</code> <br>
<code>docker run katobeke/databases-advanced-parserd</code>

##### Alle lopende containers opsommen
Om een overzicht te krijgen van de containers gebruik je het commando: <code>docker ps</code>.

##### Runnende containers stoppen
<code>docker stop databases-advanced-scraper</code> <br>
<code>docker stop katobeke/databases-advanced-parser</code>

##### Containers verwijderen
<code>docker rm databases-advanced-scraper</code> <br>
<code>docker rm databases-advanced-scraper</code>

### Network creëren en containers toevoegen
Voor meer info: https://docs.docker.com/network/bridge/
