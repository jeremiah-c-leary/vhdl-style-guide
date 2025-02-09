# -*- coding: utf-8 -*-

from vsg.token import sensitivity_clause as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import sensitivity_list


def detect(oDataStructure):
    """
    sensitivity_clause ::=
        on sensitivity_list
    """

    if oDataStructure.is_next_token("on"):
        return True
    return False


def classify_until(lUntils, oDataStructure):
    oDataStructure.replace_next_token_required("on", token.on_keyword)

    sensitivity_list.classify_until(lUntils, oDataStructure)
