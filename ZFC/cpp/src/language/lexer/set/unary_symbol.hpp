#pragma once

#include <iostream>

#include "../../text.hpp"
#include "../../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfcset {

/// @brief unary connective
class UnarySymbol : Text {
public:

    UnarySymbol(const std::string& unary_symbol);

    void make_text() override;
};

/// @brief power set
std::unique_ptr<UnarySymbol> P = std::make_unique<UnarySymbol>(POWERSET);

} // mzfclogic
} // mzfclexer
} // mzfclang
