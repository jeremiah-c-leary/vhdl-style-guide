# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import timeout_clause as token
from vsg.vhdlFile.classify import expression


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    timeout_clause ::=
        for *time*_expression
    """

    if oDataStructure.is_next_seek_token("for"):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    oDataStructure.replace_next_token_with(token.for_keyword)

    expression.classify_until(lUntils, oDataStructure)
