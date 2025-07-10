# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import enumeration_type_definition as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    enumeration_type_definition ::=
        ( enumeration_literal { , enumeration_literal } )
    """
    if oDataStructure.is_next_token("("):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.open_parenthesis)

    while not oDataStructure.is_next_token(")"):
        oDataStructure.replace_next_token_with_if(",", token.comma)
        oDataStructure.replace_next_token_with(token.enumeration_literal)

    oDataStructure.replace_next_token_with(token.close_parenthesis)
