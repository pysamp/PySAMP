#!/bin/bash
docker build \
    --platform linux/386 \
    -t pysamp/build \
    . \
&&
docker run \
    --platform linux/386 \
    --rm -ti \
    -v $PWD:/root/output \
    pysamp/build
