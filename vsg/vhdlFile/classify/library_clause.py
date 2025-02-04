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
    oDataStructure.assign_next_token_required("library", token.keyword)

    logical_name_list.classify_until([";"], oDataStructure)

    oDataStructure.assign_next_token_required(";", token.semicolon)
