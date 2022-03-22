cmake_minimum_required(VERSION 3.19)
project(Lab1)

set(CMAKE_CXX_STANDARD 20)
set(LIBRARY_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/Python/Dll)

add_library(Lab1 SHARED Algorithms/BrentAlgorithm.cpp)
set_property(TARGET Lab1 PROPERTY POSITION_INDEPENDENT_CODE ON)
set_target_properties(Lab1 PROPERTIES COMPILE_FLAGS "-m32" LINK_FLAGS "-m32")