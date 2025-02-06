# -*- coding: utf-8 -*-

from vsg.token import generic_map_aspect as token
from vsg.vhdlFile.classify import association_list


def detect(oDataStructure):
    """
    generic_map_aspect ::=
        generic map ( *generic*_association_list )
    """
    if oDataStructure.is_next_token("generic"):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.generic_keyword)
    oDataStructure.replace_next_token_required("map", token.map_keyword)
    oDataStructure.replace_next_token_required("(", token.open_parenthesis)

    association_list.classify(oDataStructure)

    oDataStructure.replace_next_token_required(")", token.close_parenthesis)
