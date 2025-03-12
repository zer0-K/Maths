#pragma once

#include <iostream>

//std::string empty_string = "";
inline const std::string& EMPTY = "";

//---------------------------------------- LANGUAGE

//-------------------- LEXER

//---------- constants

//std::string txt_empty_set = "\\emptyset";
inline const std::string& EMPTY_SET = "\\emptyset";

//---------- logic

//----- quantifiers

//std::string txt_there_is = "\\exists";
inline const std::string& EXISTS = "\\exists";

//std::string txt_forall = "\\forall";
inline const std::string& FOR_ALL = "\\forall";

//----- unary connectives

//std::string txt_not = "\\neg";
inline const std::string& NOT = "\\neg";

//----- binary connectives

//std::string txt_or = "\\lor";
inline const std::string& OR = "\\lor";

//std::string txt_and = "\\land";
inline const std::string& AND = "\\land";

//std::string txt_implies = "\\implies";
inline const std::string& IMPLIES = "\\implies";

//std::string txt_equiv = "\\iff";
inline const std::string& EQUIV = "\\iff";


//---------- set

//----- set symbols

//std::string txt_in = "\\in";
inline const std::string& IN = "\\in";

//std::string txt_included_eq = "\\subseteq";
inline const std::string& INCLUDED_EQ = "\\subseteq";

//----- unary connectives

//std::string txt_powerset = "\\mathcal(P)";
inline const std::string& POWERSET = "\\mathcal(P)";

//----- binary connectives

//std::string txt_union = "\\cup";
inline const std::string& UNION = "\\cup";

//std::string txt_intersection = "\\cap";
inline const std::string& INTER = "\\cap";
