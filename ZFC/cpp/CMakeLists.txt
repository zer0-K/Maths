cmake_minimum_required(VERSION 3.30)
project(MathsZFC)

# Prefix
if (NOT PREFIX)
    set(PREFIX ${CMAKE_CURRENT_BINARY_DIR})
endif (NOT PREFIX)
set(CMAKE_INSTALL_PREFIX ${PREFIX} CACHE STRING "Installation prefix." FORCE)

if (CXX)
    set(CMAKE_CXX_COMPILER ${CXX})
endif (CXX)

set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake ${CMAKE_MODULE_PATH})
set(CMAKE_BUILD_TYPE Debug)



# ********** all

set(HEADERS_MATHS_ZFC_ALL )
set(SOURCES_MATHS_ZFC_ALL )

add_executable(math_zfc_all src/main.cpp ${HEADERS_MATHS_ZFC_ALL} ${SOURCES_MATHS_ZFC_ALL})
