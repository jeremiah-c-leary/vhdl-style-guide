# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import secondary_unit_declaration as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    secondary_unit_declaration ::= identifier = physical_literal;
    """
    if oDataStructure.does_string_exist_before_string("=", ";"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_with(token.equal_sign)

    while not oDataStructure.is_next_token(";"):
        oDataStructure.replace_current_token_with(token.physical_literal)
    oDataStructure.replace_current_token_with(token.semicolon)
