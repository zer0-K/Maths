#pragma once

#include <iostream>

#include "../../text.hpp"
#include "../../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfclogic {

/// @brief unary connective
class UnarySymbol : Text {
public:

    UnarySymbol(const std::string& unary_symbol);

    void make_text() override;
};

/// @brief not
std::unique_ptr<UnarySymbol> neg = std::make_unique<UnarySymbol>(NOT);

} // mzfclogic
} // mzfclexer
} // mzfclang
