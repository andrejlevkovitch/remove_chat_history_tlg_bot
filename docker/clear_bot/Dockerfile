FROM debian:buster

RUN apt-get update -y &&\
    apt-get install python3 python3-pip -y &&\
    pip3 install telethon &&\
    apt-get autoremove python3-pip -y
