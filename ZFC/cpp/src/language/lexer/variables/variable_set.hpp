#pragma once

#include <iostream>

#include "../text.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfcvar {

/// @brief variable set
class VariableSet : Text {
protected:
    /// @brief id of the variable
    int _absolute_id;

    /// @brief to make the variable text, like x_1,...x_n
    int _relative_id;

    /// @brief base name, like x, y or z
    std::string _base_name;

public:

    /// @brief to attribute a unique id to a variable
    static int _id_counter;

    VariableSet(const std::string& base_name, int relative_id);

    void make_text() override;

    void set_relative_id(int i);
    void set_base_name(const std::string& base_name);
};

typedef std::unique_ptr<VariableSet> up_var;

} // mzfcvar
} // mzfclexer
} // mzfclang
