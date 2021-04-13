#Dit zijn de commando's om MongoDB te starten
sudo systemctl start mongod
sudo systemctl status mongod
sudo systemctl enable mongod
mongo --eval 'db.runCommand({ connectionStatus: 1 })'