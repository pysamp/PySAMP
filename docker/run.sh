#!/bin/sh

cd $(dirname $0)/server
pysamp_path='../build/PySAMP.so'

if [ ! -e "$pysamp_path" ]
then
    (
        cd ../build
        ./build_pysamp.sh
    ) || exit 1
    cp "$pysamp_path" ./ &&
    docker build \
        --no-cache \
        -t pysamp/server \
        . \
    &&
    rm $(basename "$pysamp_path")
fi

docker run \
    --name pysamp_server \
    -v "$PWD/../data:/server" \
    -p 7777:7777/udp \
    --rm \
    -ti \
    pysamp/server
