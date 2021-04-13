#Dit zijn de commando's die je nodig hebt om redis te installeren
sudo apt update
sudo apt install redis-server
sudo systemctl status redis-server

#Dit zijn de commando's om redis te starten
sudo systemctl start redis

#Dit is de commando om redis te stoppen 
sudo systemctl stop redis