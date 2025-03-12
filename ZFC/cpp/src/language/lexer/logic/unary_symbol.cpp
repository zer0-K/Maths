#include "unary_symbol.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfclogic {

UnarySymbol::UnarySymbol(const std::string& unary_symbol) 
{
    text = unary_symbol;
    is_made = true;
}

void UnarySymbol::make_text()
{
    
}

} // mzfclogic
} // mzfclexer
} // mzfclang
