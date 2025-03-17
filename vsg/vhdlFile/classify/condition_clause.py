# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import condition_clause as token
from vsg.vhdlFile.classify import condition


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    condition_clause ::=
        until condition
    """

    if oDataStructure.is_next_token("until"):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    oDataStructure.replace_next_token_with(token.until_keyword)

    condition.classify_until(lUntils, oDataStructure)
