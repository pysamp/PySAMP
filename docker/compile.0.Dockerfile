FROM pysamp/base:latest

RUN apt-get update
RUN apt-get install -y build-essential g++ cmake g++-multilib
RUN apt-get install -f

# WORKDIR /usr/src/pysamp
# COPY . .
# CMD [ "cmake", "./src", "-G", "Unix Makefiles", "-DCMAKE_BUILD_TYPE=Debug" ]    
