project(PySAMP)

add_compile_options(-std=c++11)


cmake_minimum_required(VERSION 3.12)
list(APPEND CMAKE_MODULE_PATH ${SAMPGDK_DIR}/cmake)

#find_package (Python3 COMPONENTS Interpreter Development)

find_package (Python 3.8.2)
find_package (PythonLibs 3.8.2)

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
  ${PYTHON_INCLUDE_DIR}
)

message(STATUS "PYTHON_LIBRARY = ${PYTHON_LIBRARY}")
message(STATUS "PYTHON_EXECUTABLE = ${PYTHON_EXECUTABLE}")
message(STATUS "PYTHON_INCLUDE_DIR = ${PYTHON_INCLUDE_DIR}")
message(STATUS "SAMPGDK_LIBRARY = ${SAMPGDK_LIBRARY}")

add_definitions(-DSAMPGDK_AMALGAMATION)

link_libraries(${PYTHON_LIBRARIES})

add_samp_plugin(PySAMP
  ${SAMPSDK_DIR}/amxplugin.cpp
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
  test/callbackstest.h
  test/callbackstest.cpp
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
