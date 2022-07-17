#!/bin/sh
docker build \
    --no-cache \
    --platform linux/amd64 \
    -t pysamp/build \
    . \
&&
docker run \
    --rm \
    --platform linux/amd64 \
    -v $PWD:/destination \
    pysamp/build \
    cp PySAMP.so /destination
