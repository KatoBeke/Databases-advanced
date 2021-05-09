sudo chmod 666 /var/run/docker.sock
docker pull katobeke/databases-advanced-scraper:latest
docker pull redis:latest
docker pull katobeke/databases-advanced-parser:latest
docker pull mongo:latest
sudo systemctl stop mongod
sudo systemctl stop redis
docker stop redis
docker stop scraper
docker stop mongo2
docker stop parser
docker rm redis
docker rm scraper
docker rm mongo2
docker rm parser
docker run -d --name redis redis
docker run -d --name scraper katobeke/databases-advanced-scraper:latest
docker run -p 27017:27017 -d --name mongo2 mongo
docker run -d --name parser katobeke/databases-advanced-parser:latest
#docker network create mynetwork
docker network connect mynetwork redis
docker network connect mynetwork scraper
docker network connect mynetwork mongo2
docker network connect mynetwork parser
sudo systemctl start redis
sudo systemctl start mongod
