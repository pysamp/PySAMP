ARG BASE

FROM $BASE

# install dependencies
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.8:i386 libpython3.8:i386
RUN apt-get update && apt-get install -y libstdc++6:i386

WORKDIR /server

CMD "./start_server.sh"