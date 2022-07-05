FROM ubuntu:22.04

ARG samp_url=http://files.sa-mp.com/samp037svr_R2-1.tar.gz
ARG crashdetect_version=4.20

ENV DEBIAN_FRONTEND=noninteractive

COPY PySAMP.so /root
COPY empty.amx /root
COPY empty.py /root
COPY server.cfg.template /root
COPY docker-entrypoint.sh /
COPY pysamp/ /root/pysamp

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
        mv /root/empty.amx gamemodes/ && \
        mv /root/PySAMP.so plugins/ && \
        export generated_password=$(python3 -c 'import os;print(os.urandom(24).hex())') && \
        envsubst < /root/server.cfg.template > server.cfg && \
        rm /root/server.cfg.template && \
        mv /root/empty.py python.py && \
        mv /root/pysamp . && \
        touch requirements.txt \
    )

VOLUME /server
WORKDIR /server

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["samp03svr"]
