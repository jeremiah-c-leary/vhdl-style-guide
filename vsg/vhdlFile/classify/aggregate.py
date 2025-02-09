# -*- coding: utf-8 -*-


def classify(oDataStructure, oTokenClass):
    """
    aggregate ::=
        ( element_association { , element_association } )
    """
    oDataStructure.replace_next_token_required("(", oTokenClass.aggregate_open_parenthesis)
    oDataStructure.replace_next_token_with(oTokenClass.simple_name)

    while oDataStructure.is_next_token(","):
        oDataStructure.replace_next_token_with(oTokenClass.aggregate_comma)
        oDataStructure.replace_next_token_with(oTokenClass.simple_name)

    oDataStructure.replace_next_token_required(")", oTokenClass.aggregate_close_parenthesis)
