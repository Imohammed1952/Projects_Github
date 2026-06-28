cmake_minimum_required(VERSION 3.16)
project(ComputerGraphics LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Build RayTracer if source exists
if(EXISTS "${CMAKE_SOURCE_DIR}/RayTracer.cc")
  add_executable(RayTracer RayTracer.cc)
endif()
