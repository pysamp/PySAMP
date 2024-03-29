FROM cheaterman/manylinux2014_i686:latest

ARG sampgdk_ref=v4.6.4
ARG pysamp_ref=v2.1.0-rc3
ARG build_type=RelWithDebInfo

WORKDIR /root

RUN \
    git clone \
        --depth 1 \
        --recursive \
        --branch ${sampgdk_ref} \
        https://github.com/Zeex/sampgdk \
    && \
    git clone \
        --depth 1 \
        --recursive \
        https://github.com/Zeex/samp-plugin-sdk \
    && \
    git clone \
        --depth 1 \
        --recursive \
        --branch ${pysamp_ref} \
        https://github.com/pysamp/PySAMP \
    && \
    ( \
        cd sampgdk && \
        export PATH="/opt/python/cp312-cp312/bin:${PATH}" && \
        sed -i 's/PythonInterp 2\.7/Python3 3.12/' CMakeLists.txt && \
        pip3.12 install --user ply && \
        chmod +x scripts/*.py{,.in} && \
        cmake \
            -S . \
            -B build \
            -DCMAKE_BUILD_TYPE=${build_type} \
            -DSAMPSDK_DIR=../samp-plugin-sdk \
            -DSAMPGDK_BUILD_AMALGAMATION=ON \
        && \
        cmake \
            --build build \
            --verbose \
        && \
        mkdir dist && \
        cd dist && \
        unzip ../build/sampgdk-*-amalgamation.zip \
    )

WORKDIR /root/PySAMP
COPY docker-entrypoint.sh /
CMD ["/docker-entrypoint.sh"]
