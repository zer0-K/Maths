#pragma once

#include <iostream>

#include "../../text.hpp"
#include "../../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfclogic {

/// @brief binary connective
class BinarySymbol : Text {
public:

    BinarySymbol(const std::string& unary_symbol);

    void make_text() override;
};


/// @brief or
std::unique_ptr<BinarySymbol> or_ = std::make_unique<BinarySymbol>(OR);

/// @brief and
std::unique_ptr<BinarySymbol> and_ = std::make_unique<BinarySymbol>(AND);

/// @brief implies
std::unique_ptr<BinarySymbol> implies = std::make_unique<BinarySymbol>(IMPLIES);

/// @brief equiv/if and only if
std::unique_ptr<BinarySymbol> iff = std::make_unique<BinarySymbol>(EQUIV);

} // mzfclogic
} // mzfclexer
} // mzfclang
