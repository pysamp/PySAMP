FROM pysamp/compile.0:latest
WORKDIR /usr/src/pysamp
COPY . .
RUN [ "cmake", "./src", "-G", "Unix Makefiles", "-DPYTHON_INCLUDE_DIR=/usr/include/python3.5m", "-DPYTHON_LIBRARY=/usr/lib/i386-linux-gnu/libpython3.5m.so", "-DCMAKE_BUILD_TYPE=Debug" ]    
CMD make; cp ./pySAMP.so /target/