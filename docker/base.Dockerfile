FROM ubuntu:xenial
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y python3.5-dev:i386
RUN apt-get install -f

RUN apt-get update && apt-get install -y build-essential g++ cmake g++-multilib git
RUN apt-get install -f

# install dependencies

RUN mkdir /root/sampgdk

RUN git clone https://github.com/Zeex/sampgdk.git /root/sampgdk
RUN git clone https://github.com/Zeex/samp-plugin-sdk.git /root/sampsdk

RUN apt-get update && apt-get install -y python2.7 python-pip
RUN pip install ply

RUN mkdir /root/sampgdk/build
RUN cd /root/sampgdk/build && cmake .. -DSAMP_SDK_ROOT=/root/sampsdk -DSAMPGDK_STATIC=ON -DSAMPGDK_BUILD_AMALGAMATION=ON
RUN cmake --build /root/sampgdk/build --config Release
RUN cmake --build /root/sampgdk/build --config Release --target install