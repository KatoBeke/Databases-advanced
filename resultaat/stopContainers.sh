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
