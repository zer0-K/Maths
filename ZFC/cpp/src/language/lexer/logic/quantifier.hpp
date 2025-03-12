#pragma once

#include <iostream>

#include "../text.hpp"
#include "../../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfclogic {

/// @brief quantifier
class Quantifier : Text {
public:

    Quantifier(const std::string& quantifier_symbol);

    void make_text() override;
};

/// @brief there exists
std::unique_ptr<Quantifier> exists = std::make_unique<Quantifier>(EXISTS);

/// @brief for all
std::unique_ptr<Quantifier> forall = std::make_unique<Quantifier>(FOR_ALL);

} // mzfclogic
} // mzfclexer
} // mzfclang
