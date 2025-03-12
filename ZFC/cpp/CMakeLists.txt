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


# ************************************************************ utils

# ****************************** constants

set(HEADERS_MATHS_ZFC_UTILS_CONST src/utils/constant/constants.hpp)
set(SOURCES_MATHS_ZFC_UTILS_CONST )

# ****************************** logging

set(HEADERS_MATHS_ZFC_UTILS_LOG src/utils/log/logger.hpp src/utils/log/log_probes.hpp)
set(SOURCES_MATHS_ZFC_UTILS_LOG src/utils/log/logger.cpp)

# ****************************** all

set(HEADERS_MATHS_ZFC_UTILS ${HEADERS_MATHS_ZFC_UTILS_LOG} ${HEADERS_MATHS_ZFC_UTILS_CONST})
set(SOURCES_MATHS_ZFC_UTILS ${SOURCES_MATHS_ZFC_UTILS_LOG} ${SOURCES_MATHS_ZFC_UTILS_CONST})

# ************************************************************ language

# ****************************** lexer

# ********** constants

set(HEADERS_MATHS_ZFC_LEXER_CONST 
    src/language/lexer/constants/constant_set.hpp
)
set(SOURCES_MATHS_ZFC_LEXER_CONST 
    src/language/lexer/constants/constant_set.cpp
)

# ********** variables

set(HEADERS_MATHS_ZFC_LEXER_VAR 
    src/language/lexer/variables/variable_set.hpp
)
set(SOURCES_MATHS_ZFC_LEXER_VAR 
    src/language/lexer/variables/variable_set.cpp
)

# ********** logic

set(HEADERS_MATHS_ZFC_LEXER_LOGIC 
    src/language/lexer/logic/quantifier.hpp src/language/lexer/logic/unary_symbol.hpp src/language/lexer/logic/binary_symbol.hpp
)
set(SOURCES_MATHS_ZFC_LEXER_LOGIC 
    src/language/lexer/logic/quantifier.cpp src/language/lexer/logic/unary_symbol.cpp src/language/lexer/logic/binary_symbol.cpp
)

# ********** set

set(HEADERS_MATHS_ZFC_LEXER_SET 
    src/language/lexer/set/inclusion.hpp src/language/lexer/set/unary_symbol.hpp src/language/lexer/set/binary_symbol.hpp 
)
set(SOURCES_MATHS_ZFC_LEXER_SET 
    src/language/lexer/set/inclusion.cpp src/language/lexer/set/unary_symbol.cpp src/language/lexer/set/binary_symbol.cpp 
)


# ********** all

set(HEADERS_MATHS_ZFC_LEXER src/language/lexer/text.hpp
    ${HEADERS_MATHS_ZFC_LEXER_CONST} ${HEADERS_MATHS_ZFC_LEXER_VAR} ${HEADERS_MATHS_ZFC_LEXER_LOGIC} ${HEADERS_MATHS_ZFC_LEXER_SET}
)
set(SOURCES_MATHS_ZFC_LEXER src/language/lexer/text.cpp
    ${SOURCES_MATHS_ZFC_LEXER_CONST} ${SOURCES_MATHS_ZFC_LEXER_VAR} ${SOURCES_MATHS_ZFC_LEXER_LOGIC} ${SOURCES_MATHS_ZFC_LEXER_SET}
)

# ****************************** all

set(HEADERS_MATHS_ZFC_LANGUAGE 
    ${HEADERS_MATHS_ZFC_LEXER}
)
set(SOURCES_MATHS_ZFC_LANGUAGE 
    ${SOURCES_MATHS_ZFC_LEXER}
)

# ************************************************************ all

set(HEADERS_MATHS_ZFC_ALL ${HEADERS_MATHS_ZFC_UTILS} ${HEADERS_MATHS_ZFC_LANGUAGE})
set(SOURCES_MATHS_ZFC_ALL ${SOURCES_MATHS_ZFC_UTILS} ${SOURCES_MATHS_ZFC_LANGUAGE})

add_executable(math_zfc_all src/main.cpp ${HEADERS_MATHS_ZFC_ALL} ${SOURCES_MATHS_ZFC_ALL})
target_link_libraries(math_zfc_all ${LIBS})
