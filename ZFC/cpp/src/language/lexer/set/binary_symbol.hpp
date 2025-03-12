#pragma once

#include <iostream>

#include "../../text.hpp"
#include "../../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfcset {

/// @brief binary connective
class BinarySymbol : Text {
public:

    BinarySymbol(const std::string& unary_symbol);

    void make_text() override;
};


/// @brief union
std::unique_ptr<BinarySymbol> U = std::make_unique<BinarySymbol>(UNION);

/// @brief intersection
std::unique_ptr<BinarySymbol> inter = std::make_unique<BinarySymbol>(INTER);

} // mzfcset
} // mzfclexer
} // mzfclang
