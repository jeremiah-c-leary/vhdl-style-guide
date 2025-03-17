# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import generic_clause as token
from vsg.vhdlFile.classify import generic_list


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    generic_clause ::=
        generic ( generic_list ) ;
    """
    return oDataStructure.are_next_consecutive_tokens(["generic", "("])


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("generic", token.generic_keyword)
    oDataStructure.replace_next_token_required("(", token.open_parenthesis)

    generic_list.classify(oDataStructure)

    oDataStructure.replace_next_token_required(")", token.close_parenthesis)
    oDataStructure.replace_next_token_required(";", token.semicolon)
