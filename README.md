# Databases-advanced
# Opdracht 1: Scraper (scraper.py)
Ik heb de volgende website gebruikt om te scrapen: https://www.blockchain.com/btc/unconfirmed-transactions <br>
Ik heb hiervan de hash, time, btc en usd gescrapet. Daarna heb ik de hash, time, btc en usd van de meest waardevolle Hash voor Bitcoin per minuut in USD gezocht en dit in een dataframe gezet. Tenslotte heb ik dit dan toegevoegd aan result.log.

## Ubuntu
Het doel van deze opdracht is om de scraper te runnen op Ubuntu Virtual Machine. 
Ik heb mijn script op mijn Windows pc gemaakt. Daarna heb ik deze repository gedownload op Ubuntu via de commando git clone met de link https://github.com/KatoBeke/Databases-advanced.git. <br> 

Om het script **scraper.py** te kunnen gebruiken moet je python runnen. Ik raad je de laatste versie van Python (3.9.2) aan. Om python te installeren gebruik je de commando sudo apt install python3. <br>
Daarnaast moet je ook pip, pandas en bs4 installeren. Je kan dit doen door de volgende commando's te typen in je Python terminal:
* sudo apt install python3-pip
* pip3 install pandas
* pip3 install bs4 

Het is ook heel belangrijk dat als je het script **scraper.py** wil runnen je in dezelfde map zit als waar **scraper.py** staat. Om naar dezelfde map te gaan typ je cd gevolgd door de naam van je repository in Github (bij mij is dit dan cd Databases-advanced). <br>
Om het script **scraper.py** te kunnen runnen gebruik je de commando python3 scraper.py. Om de uitvoering van het script te stoppen, typ je ctrl + c. in de terminal.

# Opdracht 2: Mongo (mongo.py en mongo.sh)
Het doel van deze opdracht is de data uit de vorige opdracht in MongoDB plaatsen. 

## Ubuntu
Ik gebruik nog altijd Ubuntu. Zorg er zeker voor dat je jouw git op Ubuntu hebt geüpdatet!!! Dit doe je via de commando git pull met de link https://github.com/KatoBeke/Databases-advanced.git. <br> 
### MongoDB
Om **MongoDB** te installeren moet je de volgende commando's gebruiken (of gebruik **bash.sh** van de map Bash scripts):
* sudo apt-get install gnupg
* wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
* echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
* sudo apt-get update
* sudo apt-get install -y mongodb-org
* sudo systemctl daemon-reload

Om **MongoDB** te starten gebruik je de commando's (of gebruik **mongo.sh** van de map Bash scripts):
* sudo systemctl start mongod
* sudo systemctl status mongod

Ik heb mijn scraper aangepast en dit een nieuwe naam gegeven namelijk **mongo.py**. <br>
Om **mongo.py** te kunnen gebruiken en dus mongo te runnen, moet je de volgende commando's gebruiken:
* pip3 install pymongo 
* cd < mongodb installation dir >/ bin
* mongo

Het is ook heel belangrijk dat als je het script mongo.py wil runnen je in dezelfde map zit als waar mongo.py staat. Om naar dezelfde map te gaan typ je cd gevolgd door de naam van je repository in Github (bij mij is dit dan cd Databases-advanced). <br>
Om het script **mongo.py** te kunnen runnen gebruik je de commando python3 mongo.py. Om de uitvoering van het script te stoppen, typ je ctrl + c. in de terminal.

### MongoDB Compass
Als u een visuele interface wilt, kunt u MongoDB Compass installeren. Hiervoor gebruik je de volgende commando's: 
* apt-get update
* wget https://dowloads.mongodb.com/compass/mongodb-compass_1.26.1_amd64.deb
* sudo dpkg -i mongodb-compass_1.26.1_amd64.deb

Ga nu naar applications op Ubuntu en selecteer MongoDB Compass. MongoDB Compass wordt geopend. 
Om te connecteren klik je op Connect en Connect to... Je kan op 2 manieren connecteren:
* door een connectie string te plakken in de balk die er verschijnt en dan op Connect te drukken of
* klik op Fill in connection fields individually. Er verschijnt een scherm waar je hostname en port kan invullen. Ik heb bij hostname localhost ingevuld en bij port 27017. Verder heb ik ook SRV record afgevinkt en authentication op None gezet. Druk op Connect.

Nu krijg je een overzicht van alle databases. Zodra je op een database klikt krijg je een scherm met de collections van die database.

Ik heb op de database highest_hashes gedrukt en op de collection values. Nu wordt elke minuut de meest waardevolle Hash voor Bitcoin per minuut in USD aan deze database en collection toegevoegd. Het ziet er uit als een json-file:
![image](https://user-images.githubusercontent.com/74418649/114557525-0cca8f00-9c6a-11eb-9eb4-9b70f092727d.png)

# Opdracht 3: Redis

# Opdracht 4: Docker Images

# Opdracht 5: Container Orchestration
