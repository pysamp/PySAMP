#!/bin/bash

# build PySAMP
./make.sh

# create server dir if it doesn't exist
if [[ ! -d ../server ]]; then
    mkdir ../server
    cd ../server
    wget http://files.sa-mp.com/samp037svr_R2-1.tar.gz
    tar xvf samp037svr_R2-1.tar.gz
    mv samp03/* ./
    rm -rf samp03
    cd ../docker
fi

# add empty gamemode if it doesn't exist
if [[ ! -f ../server/gamemodes/empty.amx ]]; then
    cp ./scripts/empty.amx ../server/gamemodes/
fi

# create plugins folder
if [[ ! -d ../server/plugins ]]; then
    mkdir ../server/plugins
fi

# copy plugin to server
cp ../target/PySAMP.so ../server/plugins/

# create python gamemode directory (if it doesn't exist)
if [[ ! -d ../server/python ]]; then
    mkdir ../server/python
    cp -r ../gamemodes/empty/* ../server/python
fi

# copy start script to server
cp scripts/start_server.sh ../server
chmod +x ../server/start_server.sh

# add plugin to server config and set password if it's still changeme
python3 scripts/check_server_config.py ../server/


docker build -f ./server.Dockerfile -t pysamp/server --build-arg BASE=ubuntu:bionic ../
docker run --name pysamp_server -v "$(cd ../ && pwd)"/server:/server -p 7777:7777 -p 7777:7777/udp --rm -it pysamp/server
