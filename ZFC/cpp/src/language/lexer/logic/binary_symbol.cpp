#include "binary_symbol.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfclogic {

BinarySymbol::BinarySymbol(const std::string& unary_symbol) 
{
    text = unary_symbol;
    is_made = true;
}

void BinarySymbol::make_text()
{
    
}

} // mzfclogic
} // mzfclexer
} // mzfclang
