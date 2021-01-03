ARG BASE

FROM $BASE

# install dependencies
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.8:i386 libpython3.8:i386 python3-pip
RUN apt-get update && apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386 

RUN python3.8 -m pip install --upgrade pip && \
    python3.8 -m pip install --no-cache-dir numpy tornado # TODO: make dependencies configurable

WORKDIR /server

CMD ["/bin/bash", "-c", "./samp03svr 2>&1 "]