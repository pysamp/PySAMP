cmake_minimum_required(VERSION 3.15)
project(PySAMP)

list(APPEND CMAKE_MODULE_PATH ${SAMPGDK_DIR}/cmake)
include(AMXConfig)
include(AddSAMPPlugin)
include(FindSAMPSDK)

set(PYSAMP_MAJOR_VERSION 2)
set(PYSAMP_MINOR_VERSION 1)
set(PYSAMP_REVISION 0)

set(PYSAMP_VERSION "${PYSAMP_MAJOR_VERSION}.${PYSAMP_MINOR_VERSION}.${PYSAMP_REVISION}")
add_definitions(-DPYSAMP_VERSION=${PYSAMP_VERSION})

if(MSVC)
    set(CMAKE_CXX_STANDARD 20)
else()
    set(CMAKE_CXX_STANDARD 11)
endif()

add_samp_plugin(PySAMP
    ${SAMPGDK_DIR}/build/lib/sampgdk/sampgdk.c
    ${SAMPGDK_DIR}/build/lib/sampgdk/sampgdk.h
    ${SAMPSDK_DIR}/amxplugin.cpp
    ${CMAKE_BINARY_DIR}/generated/config.h
    main.h
    main.cpp
    main.def
    pysamp/pysamp.cpp
    pysamp/pysamp.h
    pysamp/pygamemode.cpp
    pysamp/pygamemode.h
    pysamp/timer.cpp
    pysamp/timer.h
    pysamp/callbacks.cpp
    pysamp/callbacks.h
    pysamp/param_converter.cpp
    pysamp/param_converter.h
    bindings/samp.cpp
    bindings/samp.h
    bindings/logprintf.cpp
    bindings/logprintf.h
)

if(MSVC AND NOT CMAKE_BUILD_TYPE MATCHES "Debug")
    find_package(
        Python3
        COMPONENTS Development.SABIModule
        REQUIRED
    )
    message(STATUS "Python3_INCLUDE_DIRS = ${Python3_INCLUDE_DIRS}")
    message(STATUS "Python3_SABI_LIBRARIES = ${Python3_SABI_LIBRARIES}")
    target_link_libraries(PySAMP Python3::SABIModule)
else()
    find_package(
        Python3
        COMPONENTS Development.Embed
        REQUIRED
    )
    message(STATUS "Python3_INCLUDE_DIRS = ${Python3_INCLUDE_DIRS}")
    message(STATUS "Python3_LIBRARIES = ${Python3_LIBRARIES}")
    target_link_libraries(PySAMP Python3::Python)
endif()

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${SAMPSDK_DIR}/amx
    ${SAMPGDK_DIR}/build/lib/sampgdk/
    ${SAMPSDK_INCLUDE_DIR}
    ${CMAKE_CURRENT_SOURCE_DIR}/bindings
    ${CMAKE_CURRENT_SOURCE_DIR}/pysamp
    ${Python3_INCLUDE_DIRS}
    ${CMAKE_BINARY_DIR}/generated/
)

add_definitions(-DSAMPGDK_AMALGAMATION)

configure_file(config.h.in ${CMAKE_BINARY_DIR}/generated/config.h)

find_package(Doxygen)
if(DOXYGEN_FOUND)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
    add_custom_target(doc
        ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
        WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
        COMMENT "Generating API documentation with Doxygen" VERBATIM
    )
endif(DOXYGEN_FOUND)
