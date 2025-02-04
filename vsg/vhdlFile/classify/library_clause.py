# -*- coding: utf-8 -*-

from vsg.token import library_clause as token
from vsg.vhdlFile.classify import logical_name_list


def detect(oDataStructure):
    """
    library_clause ::=
        library logic_name_list ;
    """
    if oDataStructure.is_next_token("library"):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_current_token_with(token.keyword)

    logical_name_list.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
