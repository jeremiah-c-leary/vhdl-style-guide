# -*- coding: utf-8 -*-

from vsg.token import port_clause as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import port_list


def detect(oDataStructure):
    """
    port_clause ::=
        port ( port_list ) ;
    """

    if oDataStructure.are_next_consecutive_tokens(["port", "("]):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.port_keyword)
    oDataStructure.replace_next_token_with(token.open_parenthesis)

    port_list.classify(oDataStructure)

    oDataStructure.replace_next_token_required(")", token.close_parenthesis)
    oDataStructure.replace_next_token_required(";", token.semicolon)
