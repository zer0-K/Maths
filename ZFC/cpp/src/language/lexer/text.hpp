#pragma once

#include <iostream>
#include <memory>

namespace mzfclang {
namespace mzfclexer {

/// @brief any object of the language is a text
class Text {
protected:
    bool is_made;

    std::string text;
    
public:

    Text();

    virtual void make_text() = 0;

    std::string get_text();

    void reset();
};

typedef std::unique_ptr<Text> up_txt;

} // mzfclexer
} // mzfclang
