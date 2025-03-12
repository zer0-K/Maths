#include "variable_set.hpp"

#include "../../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfcvar {

int VariableSet::_id_counter = 0;

VariableSet::VariableSet(const std::string& base_name, int relative_id = -1) 
{
    _base_name = base_name;
    _relative_id = relative_id;

    _absolute_id = VariableSet::_id_counter;
    VariableSet::_id_counter++;

    make_text();
}

void VariableSet::make_text()
{
    text = _base_name;

    if(_relative_id != -1)
    {
        // x_{i}
        text += "_{" + std::to_string(_relative_id) + "}";
    }
}

} // mzfcvar
} // mzfclexer
} // mzfclang
