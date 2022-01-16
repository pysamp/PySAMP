#!/bin/sh
docker build \
    --no-cache \
    -t pysamp/build \
    . \
&&
docker run \
    --rm \
    -v $PWD:/destination \
    pysamp/build \
    cp PySAMP.so /destination
