#include "constant_set.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfcconst {

ConstantSet::ConstantSet(const std::string& set_name) 
{
    text = set_name;
    is_made = true;
}

void ConstantSet::make_text()
{
    
}

} // mzfcconst
} // mzfclexer
} // mzfclang
