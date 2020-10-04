docker build -f ./make.Dockerfile -t pysamp/make --build-arg BASE=ubuntu:bionic ../

#docker build -f ./base.Dockerfile -t pysamp/eoan --build-arg BASE=ubuntu:eoan ../
#docker build -f ./base.Dockerfile -t pysamp/focal --build-arg BASE=ubuntu:focal ../

#docker build -f ./base.Dockerfile -t pysamp/stretch --build-arg BASE=debian:stretch ../
#docker build -f ./base.Dockerfile -t pysamp/buster --build-arg BASE=debian:buster ../

docker run --name pysamp -v "$(cd ../ && pwd)"/target:/target --rm pysamp/make
