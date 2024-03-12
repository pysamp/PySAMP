FROM ubuntu:22.04

ARG samp_url=https://gta-multiplayer.cz/downloads/samp037svr_R2-2-1.tar.gz
ARG crashdetect_version=4.20

ENV DEBIAN_FRONTEND=noninteractive

RUN \
    dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-dev:i386 \
        python3-pip \
        gcc-i686-linux-gnu \
        g++-i686-linux-gnu \
        libc6:i386 \
        libstdc++6:i386 \
        wget \
        gettext-base \
    && \
    mkdir /default_server && \
    ( \
        cd /default_server && \
        wget ${samp_url} -O server.tar.gz && \
        tar xf server.tar.gz && \
        rm server.tar.gz && \
        ls -lah samp03 && \
        mv samp03/announce samp03/samp-npc samp03/samp03svr ./ && \
        rm -rf samp03 && \
        mkdir gamemodes plugins scriptfiles && \
        wget https://github.com/Zeex/samp-plugin-crashdetect/releases/download/v${crashdetect_version}/crashdetect-${crashdetect_version}-linux.tar.gz && \
        tar xf crashdetect-${crashdetect_version}-linux.tar.gz && \
        rm crashdetect-${crashdetect_version}-linux.tar.gz && \
        mv crashdetect-${crashdetect_version}-linux/crashdetect.so plugins/ && \
        rm -rf crashdetect-${crashdetect_version}-linux && \
        touch requirements.txt \
    )

COPY server.cfg.template /root
RUN \
    cd /default_server && \
    export generated_password=$(python3 -c 'import os;print(os.urandom(24).hex())') && \
    envsubst < /root/server.cfg.template > server.cfg && \
    rm /root/server.cfg.template

COPY empty.amx /default_server/gamemodes
COPY empty.py /default_server/python.py
COPY docker-entrypoint.sh /
COPY pysamp/ /default_server/pysamp
COPY PySAMP.so /default_server/plugins

VOLUME /server
WORKDIR /server

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["samp03svr"]
