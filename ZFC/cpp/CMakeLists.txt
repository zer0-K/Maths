cmake_minimum_required(VERSION 3.30)
project(MathsZFC)

# forder use c++ 23
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

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


# ********** utils

set(HEADERS_MATHS_ZFC_UTILS src/utils/log/logger.hpp src/utils/log/log_probes.hpp)
set(SOURCES_MATHS_ZFC_UTILS src/utils/log/logger.cpp)


# ********** all

set(HEADERS_MATHS_ZFC_ALL ${HEADERS_MATHS_ZFC_UTILS})
set(SOURCES_MATHS_ZFC_ALL ${SOURCES_MATHS_ZFC_UTILS})

add_executable(math_zfc_all src/main.cpp ${HEADERS_MATHS_ZFC_ALL} ${SOURCES_MATHS_ZFC_ALL})
target_link_libraries(math_zfc_all ${LIBS})
