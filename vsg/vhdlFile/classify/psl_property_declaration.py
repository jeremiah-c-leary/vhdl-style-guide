# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import property_declaration as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    psl_clock_declaration ::=
        property PSL_Identifier [ { Formal_Parameter_List ) ] DEF_SYM Property ;
    """

    if oDataStructure.is_next_token("property"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("property", token.property_keyword)
    while not oDataStructure.is_next_token(";"):
        oDataStructure.replace_next_token_with(token.todo)

    oDataStructure.replace_next_token_required(";", token.semicolon)
