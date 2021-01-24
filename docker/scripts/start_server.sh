#!/bin/bash
export LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/lib

./samp03svr > pysamp.log #valgrind ... 2>&1 
#./samp03svr