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
  ${CMAKE_CURRENT_SOURCE_DIR}/bindings
  ${CMAKE_CURRENT_SOURCE_DIR}/pySAMP
  ${PYTHON_INCLUDE_DIR}
)

add_definitions(-DSAMPGDK_AMALGAMATION)

link_libraries(${PYTHON_LIBRARIES})

add_samp_plugin(pySAMP
  amxplugin.cpp
  main.cpp
  main.def
  sampgdk.c
  sampgdk.h
  pysamp/PySAMP.cpp
  pysamp/PySAMP.h
  pysamp/PyGamemode.cpp
  pysamp/PyGamemode.h
  bindings/callbacks.h
  bindings/samp.h
  bindings/const.h
  bindings/const.cpp
  test/callbackstest.h
  test/callbackstest.cpp
)

find_package(Doxygen)
if(DOXYGEN_FOUND)
  configure_file(${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile.in ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile @ONLY)
  add_custom_target(doc
    ${DOXYGEN_EXECUTABLE} ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    COMMENT "Generating API documentation with Doxygen" VERBATIM
  )
endif(DOXYGEN_FOUND)
