FROM ubuntu:rolling

ARG sampgdk_version=4.6.2
ARG pysamp_branch=main
ARG build_type=Release
ARG job_count=4

WORKDIR /root
ENV DEBIAN_FRONTEND=noninteractive

RUN \
    dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        g++-multilib \
        cmake \
        git \
        ca-certificates \
        wget \
    && \
    git clone \
        --depth 1 \
        --recursive \
        --branch v${sampgdk_version} \
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
        --branch ${pysamp_branch} \
        https://github.com/habecker/PySAMP \
    && \
    mkdir sampgdk/build && \
    ( \
        cd sampgdk/build && \
        apt-get install -y --no-install-recommends python2 && \
        wget https://bootstrap.pypa.io/pip/2.7/get-pip.py -O- | python2 && \
        python2 -mpip install --user ply && \
        cmake \
            .. \
            -G 'Unix Makefiles' \
            -DCMAKE_BUILD_TYPE=${build_type} \
            -DSAMPSDK_DIR=../../samp-plugin-sdk \
            -DSAMPGDK_BUILD_AMALGAMATION=ON \
        && \
        make && \
        apt-get remove -y --purge python2 && \
        rm -rf \
            /usr/local/bin/* \
            /usr/local/lib/python2.7 \
    ) && \
    mkdir PySAMP/build && \
    ( \
        cd PySAMP/build && \
        apt-get install -y --no-install-recommends python3-dev:i386 && \
        cmake \
            ../src \
            -DCMAKE_BUILD_TYPE=${build_type} \
            -DSAMPSDK_DIR=../../samp-plugin-sdk \
            -DSAMPGDK_DIR=../../sampgdk \
            -DSAMPGDK_LIBRARY=../../sampgdk/build/libsampgdk.so \
            -DPython3_ROOT_DIR=$(python3-config --configdir) \
        && \
        make -j${job_count} && \
        mv PySAMP.so ../.. && \
        apt-get remove -y --purge python3-dev:i386 \
    ) && \
    apt-get remove -y --allow-remove-essential --purge \
        build-essential \
        g++-multilib \
        cmake \
        git \
        ca-certificates \
        wget \
        $(apt-mark showauto) \
    && \
    dpkg --remove-architecture i386 && \
    rm -rf \
        samp-plugin-sdk \
        sampgdk \
        PySAMP \
        /root/.cache \
        /root/.local \
        /var/lib/apt \
    ;
