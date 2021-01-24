#!/bin/bash

# build PySAMP
./make.sh

# create server dir if it doesn't exist
if [[ ! -d ../server ]]; then
    mkdir ../server
    cd ../server
    wget http://files.sa-mp.com/samp037svr_R3.tar.gz
    tar xvf samp037svr_R3.tar.gz
    mv samp03/* ./
    rm -rf samp03
    cd ../docker
fi

# create plugins folder
if [[ ! -d ../server/plugins ]]; then
    mkdir ../server/plugins
fi

# add crashdetect plugin to server
if [[ ! -f ../server/plugins/crashdetect.so ]]; then
    cd ../server/plugins
    wget https://github.com/Zeex/samp-plugin-crashdetect/releases/download/v4.20/crashdetect-4.20-linux.tar.gz
    tar xvf crashdetect-4.20-linux.tar.gz
    rm crashdetect-4.20-linux.tar.gz
    mv crashdetect-4.20-linux/crashdetect.so ./
    rm -rf crashdetect-4.20-linux/
    cd ../../docker
fi

# add empty gamemode if it doesn't exist
if [[ ! -f ../server/gamemodes/empty.amx ]]; then
    cp ./scripts/empty.amx ../server/gamemodes/
fi
# add empty filterscript if it doesn't exist
if [[ ! -f ../server/filterscripts/empty.amx ]]; then
    cp ./scripts/empty_filterscript.amx ../server/filterscripts/empty.amx
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
