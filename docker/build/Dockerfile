FROM quay.io/pypa/manylinux2014_i686:2023-04-09-db9a92f

ARG sampgdk_ref=v4.6.2
ARG pysamp_ref=v2.1.0-rc2
ARG build_type=Release

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
    mkdir sampgdk/build && \
    ( \
        cd sampgdk/build && \
        curl https://bootstrap.pypa.io/pip/2.7/get-pip.py | python2 && \
        python2 -mpip install --user ply==3.10 && \
        cmake \
            .. \
            -G 'Unix Makefiles' \
            -DCMAKE_BUILD_TYPE=${build_type} \
            -DSAMPSDK_DIR=../../samp-plugin-sdk \
            -DSAMPGDK_BUILD_AMALGAMATION=ON \
        && \
        make -j$(nproc) \
    )

WORKDIR /root/PySAMP
COPY docker-entrypoint.sh /
CMD ["/docker-entrypoint.sh"]
