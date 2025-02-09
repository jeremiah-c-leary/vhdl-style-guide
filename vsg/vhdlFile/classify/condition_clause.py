# -*- coding: utf-8 -*-

from vsg.token import condition_clause as token
from vsg.vhdlFile.classify import condition


def detect(oDataStructure):
    """
    condition_clause ::=
        until condition
    """

    if oDataStructure.is_next_token("until"):
        return True
    return False


def classify_until(lUntils, oDataStructure):
    oDataStructure.replace_next_token_with(token.until_keyword)

    condition.classify_until(lUntils, oDataStructure)
