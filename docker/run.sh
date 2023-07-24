#!/bin/sh

cd $(dirname $0)/server
pysamp_path='../build/python3.10/PySAMP.so'
pysamp_module_path='../../pysamp'

if [ ! -e "$pysamp_path" ]
then
    (
        cd ../build
        ./build.sh
    ) || exit 1
    cp "$pysamp_path" ./ &&
    cp -r "$pysamp_module_path" ./ &&
    docker build \
        --no-cache \
        --platform linux/amd64 \
        -t pysamp/server \
        . \
    &&
    rm $(basename "$pysamp_path")
    rm -rf "./pysamp"
fi

docker run \
    --name pysamp_server \
    --platform linux/amd64 \
    -v "$PWD/../data:/server" \
    -p 7777:7777/udp \
    --rm \
    -ti \
    pysamp/server
