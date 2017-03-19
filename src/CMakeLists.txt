project(pySAMP)

cmake_minimum_required(VERSION 2.8)
list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake)

find_package ( PythonInterp 3.6)
find_package ( PythonLibs 3.6)

include(AMXConfig)
include(AddSAMPPlugin)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/amx
  ${PYTHON_INCLUDE_DIR}
)

add_definitions(-DSAMPGDK_AMALGAMATION -DPYTHON)

add_samp_plugin(pySAMP
  amxplugin.cpp
  pySAMP.cpp
  pySAMP.def
  sampgdk.c
  sampgdk.h
)