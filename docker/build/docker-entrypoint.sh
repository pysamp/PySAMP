#!/bin/bash
targets=(
    cp36-cp36m
    cp37-cp37m
    cp38-cp38
    cp39-cp39
    cp310-cp310
    cp311-cp311
)
libs_archive=/opt/_internal/static-libs-for-embedding-only.tar.xz
libcrypt_path=/usr/local/lib/libcrypt.so
config="${CONFIG:-Release}"

if [[ -e "${libs_archive}" ]]; then
    (
        cd /opt/_internal
        tar xf "${libs_archive}"
        rm "${libs_archive}"
    )
fi

if grep '.so.2' "${libcrypt_path}"; then
    # Force linking against libcrypt.so.1
    cp "${libcrypt_path}"{.1,}
    ldconfig
fi

for target in "${targets[@]}"; do
    (
        echo "Building for ${target}..."
        export PATH="/opt/python/${target}/bin:${PATH}"
        build_dir="build_${target}"
        target_dir="../output/python3.$(python3 -c 'import sys; print(sys.version_info[1])')"
        cmake \
            -S src \
            -B "build_${target}" \
            -D SAMPSDK_DIR="${PWD}/../samp-plugin-sdk" \
            -D SAMPGDK_DIR="${PWD}/../sampgdk" \
            -D CMAKE_BUILD_TYPE="${config}" \
        &&
        cmake \
            --build ${build_dir} \
            --config "${config}" \
            --parallel $(nproc) \
        &&
        mkdir -p ${target_dir} &&
        cp "${build_dir}/PySAMP.so" ${target_dir}
    )
done
