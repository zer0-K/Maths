#pragma once

#include <iostream>

#include "../../text.hpp"
#include "../../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfcconst {

/// @brief constant set
class ConstantSet : Text {
public:

    ConstantSet(const std::string& set_name);

    void make_text() override;
};

/// @brief empty set
std::unique_ptr<ConstantSet> mpty = std::make_unique<ConstantSet>(EMPTY_SET);

} // mzfcconst
} // mzfclexer
} // mzfclang
