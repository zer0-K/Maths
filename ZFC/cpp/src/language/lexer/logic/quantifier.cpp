#include "quantifier.hpp"

namespace mzfclang {
namespace mzfclexer {
namespace mzfclogic {

Quantifier::Quantifier(const std::string& quantifier_symbol) 
{
    text = quantifier_symbol;
    is_made = true;
}

void Quantifier::make_text()
{
    
}

} // mzfclogic
} // mzfclexer
} // mzfclang
