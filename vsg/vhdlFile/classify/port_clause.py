# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import port_clause as token
from vsg.vhdlFile.classify import port_list


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    port_clause ::=
        port ( port_list ) ;
    """
    return oDataStructure.are_next_consecutive_tokens(["port", "("])


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.port_keyword)
    oDataStructure.replace_next_token_with(token.open_parenthesis)

    port_list.classify(oDataStructure)

    oDataStructure.replace_next_token_required(")", token.close_parenthesis)
    oDataStructure.replace_next_token_required(";", token.semicolon)
