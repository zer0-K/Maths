#include "inclusion.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfcset {

InclusionSymbol::InclusionSymbol(const std::string& unary_symbol) 
{
    text = unary_symbol;
    is_made = true;
}

void InclusionSymbol::make_text()
{
    
}

} // mzfcset
} // mzfclexer
} // mzfclang
