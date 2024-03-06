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
        export PATH="/opt/python/cp311-cp311/bin:${PATH}" && \
        sed -i s/2.7/3.11/ CMakeLists.txt && \
        pip install --user ply==3.4 && \
        cmake \
            -S . \
            -B build \
            -G 'Unix Makefiles' \
            -DCMAKE_BUILD_TYPE=${build_type} \
            -DSAMPSDK_DIR=../samp-plugin-sdk \
            -DSAMPGDK_BUILD_AMALGAMATION=ON \
        && \
        cmake \
            --build build \
            --parallel $(nproc) \
    )

WORKDIR /root/PySAMP
COPY docker-entrypoint.sh /
CMD ["/docker-entrypoint.sh"]
