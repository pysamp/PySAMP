FROM ubuntu:xenial
RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y python3.5-dev:i386
RUN apt-get install -f