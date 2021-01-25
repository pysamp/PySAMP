project(PySAMP)

add_compile_options(-std=c++11)

cmake_minimum_required(VERSION 3.7)
list(APPEND CMAKE_MODULE_PATH ${SAMPGDK_DIR}/cmake)


set(PYSAMP_MAJOR_VERSION 1)
set(PYSAMP_MINOR_VERSION 2)
set(PYSAMP_REVISION 0)

set(PYSAMP_VERSION "${PYSAMP_MAJOR_VERSION}.${PYSAMP_MINOR_VERSION}.${PYSAMP_REVISION}")
set(PYTHON_VERSION "PYTHON_VERSION" CACHE STRING "The version of python to use (eg. 3.8)")
set(PYTHON_STATIC_LIBRARY "PYTHON_STATIC_LIBRARY" CACHE STRING "The name of the python library to use (eg. libpython3.8.so.1.0") 


add_definitions( -DPYTHON_VERSION=${PYTHON_VERSION} )
add_definitions( -DPYSAMP_VERSION=${PYSAMP_VERSION} )

find_package (PythonInterp ${PYTHON_VERSION} REQUIRED)
find_package (PythonLibs ${PYTHON_VERSION} REQUIRED)

find_library (SAMPGDK_LIBRARY
    NAMES sampgdk sampgdk4s
    HINTS "${CMAKE_PREFIX_PATH}/lib/")

include(AMXConfig)
include(AddSAMPPlugin)
include(FindSAMPSDK)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${SAMPSDK_DIR}/amx
  ${SAMPGDK_DIR}/build/lib/sampgdk/
  ${SAMPSDK_INCLUDE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/bindings
  ${CMAKE_CURRENT_SOURCE_DIR}/pysamp
  ${PYTHON_INCLUDE_DIRS}
  ${CMAKE_BINARY_DIR}/generated/
)

message(STATUS "PYTHON_LIBRARY = ${PYTHON_LIBRARY}")
message(STATUS "PYTHON_EXECUTABLE = ${PYTHON_EXECUTABLE}")
message(STATUS "PYTHON_INCLUDE_DIRS = ${PYTHON_INCLUDE_DIRS}")
message(STATUS "SAMPGDK_LIBRARY = ${SAMPGDK_LIBRARY}")

add_definitions(-DSAMPGDK_AMALGAMATION)

link_libraries(${PYTHON_LIBRARIES})

configure_file( config.h.in ${CMAKE_BINARY_DIR}/generated/config.h )

add_samp_plugin(PySAMP
  ${SAMPSDK_DIR}/amxplugin.cpp
  ${CMAKE_BINARY_DIR}/generated/config.h
  main.h
  main.cpp
  main.def
  ${SAMPGDK_DIR}/build/lib/sampgdk/sampgdk.c
  ${SAMPGDK_DIR}/build/lib/sampgdk/sampgdk.h
  pysamp/pysamp.cpp
  pysamp/pysamp.h
  pysamp/pygamemode.cpp
  pysamp/pygamemode.h
  bindings/callbacks.h
  bindings/samp.h
  bindings/const.h
  bindings/const.cpp
)

target_link_libraries(PySAMP ${SAMPGDK_LIBRARY})

find_package(Doxygen)
if(DOXYGEN_FOUND)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
  add_custom_target(doc
    ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    COMMENT "Generating API documentation with Doxygen" VERBATIM
  )
endif(DOXYGEN_FOUND)
