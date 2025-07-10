# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import clock_declaration as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    psl_clock_declaration ::=
        default clock DEF_SYM Clock_Expression ;
    """
    if oDataStructure.are_next_consecutive_tokens(["default", "clock"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("default", token.default_keyword)
    oDataStructure.replace_next_token_required("clock", token.clock_keyword)
    while not oDataStructure.is_next_token(";"):
        oDataStructure.replace_next_token_with(token.todo)

    oDataStructure.replace_next_token_required(";", token.semicolon)
