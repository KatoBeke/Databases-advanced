#Dit zijn de commando's die je nodig hebt om redis te installeren
wget http :// download . redis . io / redis - stable . tar . gz
tar xvzf redis - stable . tar . gz
cd redis - stable
make
make test

sudo apt update
sudo apt install redis-server
sudo systemctl status redis-server

#Dit zijn de commando's om redis te starten
sudo systemctl start redis
cd src
redis - server
redis - cli ping
redis - cli
redis 127.0.0.1:6379 > ping

#Dit is de commando om redis te stoppen 
sudo systemctl stop redis