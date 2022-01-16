#!/bin/sh

if [ -z "$(ls -A /server)" ]
then
    cp -r /default_server/* /server/
fi

if [ "$1" = "samp03svr" ]
then
    pip install -r /server/requirements.txt &&
    exec /server/samp03svr 2>&1
fi

exec "$@"
