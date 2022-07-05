#!/bin/sh

cd $(dirname $0)/server
pysamp_path='../build/PySAMP.so'
pysamp_module_path='../../pysamp'

if [ ! -e "$pysamp_path" ]
then
    (
        cd ../build
        ./build_pysamp.sh
    ) || exit 1
    cp "$pysamp_path" ./ &&
    cp -r "$pysamp_module_path" ./ &&
    docker build \
        --no-cache \
        -t pysamp/server \
        . \
    &&
    rm $(basename "$pysamp_path")
    rm -rf "./pysamp"
fi

docker run \
    --name pysamp_server \
    -v "$PWD/../data:/server" \
    -p 7777:7777/udp \
    --rm \
    -ti \
    pysamp/server
