FROM debian:buster

RUN apt-get update -y &&\
    apt-get install cron -y &&\
    apt-get install python3 python3-pip -y &&\
    pip3 install telethon

CMD cron
