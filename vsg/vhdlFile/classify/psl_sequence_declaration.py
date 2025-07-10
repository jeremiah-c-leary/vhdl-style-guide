# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token.psl import sequence_declaration as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    psl_sequence_declaration ::=
        sequence PSL_Identifier [ ( Formal_Parameter_List ) ] DEF_SYM Sequence ;
    """

    if oDataStructure.is_next_token("sequence"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("sequence", token.sequence_keyword)
    while not oDataStructure.is_next_token(";"):
        oDataStructure.replace_next_token_with(token.todo)

    oDataStructure.replace_next_token_required(";", token.semicolon)
