# -*- coding: utf-8 -*-
import copy

from vsg import parser
from vsg.token import sensitivity_list as token
from vsg.vhdlFile.classify import name, utils


def classify(oDataStructure):
    """
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    """

    iParen = 0
    while oDataStructure.advance_to_next_token():
        iParen = utils.update_paren_counter(iParen, oDataStructure)

        if utils.unmatched_close_paren_found(iParen):
            break

        if oDataStructure.is_next_token(","):
            oDataStructure.replace_next_token_with(token.comma)
        else:
            name.classify_until([","], oDataStructure)


def classify_until(lUntils, iToken, lObjects):
    """
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    """
    iCurrent = iToken
    iLast = 0
    lMyUntils = copy.deepcopy(lUntils)
    lMyUntils.append(",")
    while iLast != iCurrent:
        iLast = iCurrent
        if lObjects[utils.find_next_token(iCurrent, lObjects)].get_lower_value() in lUntils:
            return iCurrent
        iCurrent = utils.assign_next_token_if(",", token.comma, iCurrent, lObjects)
        iCurrent = name.classify_until(lMyUntils, iCurrent, lObjects)
