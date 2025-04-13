# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import primary_unit_declaration as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    primary_unit_declaration ::= identifier;
    """
    return classify(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    while not oDataStructure.is_next_token(";"):
        oDataStructure.replace_current_token_with(token.identifier)
    oDataStructure.replace_current_token_with(token.semicolon)
