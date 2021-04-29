FROM ubuntu:latest AS parser
COPY . .
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3-pip
RUN apt-get install -y python3
RUN git clone https://github.com/KatoBeke/Databases-advanced.git
RUN cd Databases-advanced
RUN pip3 install requests
RUN pip3 install beautifulsoup4
RUN pip3 install pandas
RUN pip3 install pymongo 
RUN pip3 install redis
RUN cp "Databases-advanced/Docker/Container-orchestration/redisToMongo.py" .
RUN python3 redisToMongo.py
CMD ["python3","redisToMongo.py"]
