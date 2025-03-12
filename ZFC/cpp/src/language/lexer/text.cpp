#include "text.hpp"

#include "../../utils/constant/constants.hpp"

namespace mzfclang {
namespace mzfclexer {

Text::Text() 
{
   is_made = false;
   text = EMPTY;
}

std::string Text::get_text()
{
    if(!is_made)
        make_text();
    
    return text;
}

void Text::reset()
{
    is_made = false;
}

} // mzfclexer
} // mzfclang
