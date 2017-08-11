#Experimental Dockerfile - for testing


# Base image
FROM mongo:3.3
MAINTAINER Paulo Silva (pmgsilva@dei.uc.pt) University of Coimbra & Eduardo Morais (eduardo.morais@gmail.com)
RUN apt-get update && apt-get -y install nano bash apt-utils sudo lftp python3

COPY ./db_scripts /db_scripts
COPY ./dump /dump
VOLUME ["/data/db"]
EXPOSE 27017

ENTRYPOINT mongod --smallfiles --rest --port 27017 --dbpath /data/db

#------------------------------------------------------------------------------------


# Base image
FROM alpine:3.4
COPY ./ /usr/src/app
WORKDIR /usr/src/app

# Installing needed packages
RUN apk add --update --no-cache python3 \
 && apk add --update --no-cache --virtual .build-deps gcc libc-dev python3 python3-dev
RUN apk update && apk add build-base libffi-dev
EXPOSE 9000

# Install requirements
ADD aaa_manager/requirements.txt /usr/src/app/aaa_manager/
RUN pip3 install --no-cache-dir -q --upgrade pip \
 && pip3 install --no-cache-dir -r aaa_manager/requirements.txt \
 && rm -rf ~/.cache/pip/*
 
#RUN python3 db_scripts/create_mongo_user.py

# Run server. gunicorn -u is need for docker-compose (needs unbuffered output)
CMD python3 setup.py develop && gunicorn --reload --log-level DEBUG --paste development.ini \
&& python3 db_scripts/create_mongo_user.py
