ARG BASE

FROM $BASE

# install dependencies
RUN dpkg --add-architecture i386
RUN apt-get -qq update && apt-get -qq install software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get -qq update && \
    apt-get -qq install libc6-dev:i386 gcc:i386 && \
    apt-get -qq install python3.8:i386 libpython3.8:i386 python3-pip && \
    apt-get -qq install python3.8-dev:i386
RUN apt-get -qq install libc6:i386 libncurses5:i386 libstdc++6:i386
RUN apt-get -qq install gcc-i686-linux-gnu

RUN python3.8 -m pip install --upgrade pip && \
    python3.8 -m pip install -r requirements.txt --no-cache-dir 
    # modules can be edited in requirements.txt. Copied from /gamemodes/empty/requirements.txt

WORKDIR /server

CMD ["/bin/bash", "-c", "./samp03svr 2>&1 "]
