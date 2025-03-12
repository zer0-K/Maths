#pragma once

#include <iostream>

#include "../../text.hpp"
#include "../../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfcset {

/// @brief unary connective
class InclusionSymbol : Text {
public:

    InclusionSymbol(const std::string& unary_symbol);

    void make_text() override;
};

/// @brief is in set
std::unique_ptr<InclusionSymbol> isin = std::make_unique<InclusionSymbol>(IN);

/// @brief is subset or equal
std::unique_ptr<InclusionSymbol> included_eq = std::make_unique<InclusionSymbol>(INCLUDED_EQ);

} // mzfclogic
} // mzfclexer
} // mzfclang
