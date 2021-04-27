FROM ubuntu:latest AS scraper
COPY . .
RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3-pip
RUN apt-get install -y python3
RUN git clone https://github.com/KatoBeke/Databases-advanced.git
RUN cd Databases-advanced
RUN pip3 install request
RUN pip3 install bs4
RUN pip3 install pandas
RUN pip3 install pymongo 
RUN pip3 install redis
RUN cp "Databases-advanced/Docker/Container Orchestration/red.py" .
CMD ["python3","red.py"]
