ARG BASE
ARG TYPE=Debug

FROM $BASE


RUN apt-get update && apt-get install -y build-essential g++ cmake g++-multilib git
RUN apt-get install -f

# install dependencies

#RUN mkdir /root/sampgdk

RUN git clone --depth 1 --branch v4.6.1 https://github.com/Zeex/sampgdk.git /root/sampgdk
#COPY docker/sampgdk/ /root/sampgdk
RUN git clone https://github.com/Y-Less/samp-plugin-sdk.git /root/sampsdk

RUN apt-get update && apt-get install -y python2.7 python-pip
RUN pip install ply

RUN mkdir /root/sampgdk/build
RUN cd /root/sampgdk/build && cmake .. -DSAMP_SDK_ROOT=/root/sampsdk -DSAMPGDK_STATIC=ON -DSAMPGDK_BUILD_AMALGAMATION=ON -DCMAKE_BUILD_TYPE=$TYPE
RUN cmake --build /root/sampgdk/build --config $TYPE
RUN cmake --build /root/sampgdk/build --config $TYPE --target install

RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y python3.8-dev:i386 libpython3.8-dev:i386
# RUN apt-get install -f

# RUN apt-get update && apt-get install -y wget

# RUN mkdir /root/python
# RUN cd /root/python && wget https://github.com/python/cpython/archive/v3.8.3.tar.gz && tar xvf v3.8.3.tar.gz

# some deps for debugging and development purposes:
RUN apt-get update && apt-get install -y gdb vim valgrind libc6-dbg:i386

WORKDIR /usr/src/pysamp
COPY . .

RUN [ "cmake", "./src", "-G", "Unix Makefiles", "-DCMAKE_BUILD_TYPE=Debug", "-DSAMPSDK_DIR=/root/sampsdk", "-DSAMPGDK_DIR=/root/sampgdk", "-DPYTHON_INCLUDE_DIRS=/usr/include/i386-linux-gnu/python3.8", "-DPYTHON_LIBRARY=/usr/lib/i386-linux-gnu/libpython3.8.so", "-DPYTHON_STATIC_LIBRARY=libpython3.8.so.1.0", "-DPYTHON_VERSION=3.8.6" ]    
CMD make; cp ./PySAMP.so /target/
