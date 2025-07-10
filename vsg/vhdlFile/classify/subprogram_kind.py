# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import subprogram_kind as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_kind ::=
        procedure | function
    """

    if oDataStructure.is_next_token("procedure"):
        return True
    if oDataStructure.is_next_token("function"):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("procedure", token.procedure_keyword)
    oDataStructure.replace_next_token_with_if("function", token.function_keyword)
