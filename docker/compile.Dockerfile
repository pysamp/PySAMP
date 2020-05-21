FROM pysamp/base:latest
WORKDIR /usr/src/pysamp
COPY . .

RUN [ "cmake", "./src", "-G", "Unix Makefiles", "-DSAMPSDK_DIR=/root/sampsdk", "-DSAMPGDK_DIR=/root/sampgdk", "-DPYTHON_INCLUDE_DIR=/usr/include/python3.5m", "-DPYTHON_LIBRARY=/usr/lib/i386-linux-gnu/libpython3.5m.so", "-DCMAKE_BUILD_TYPE=Debug" ]    
CMD make; cp ./PySAMP.so /target/