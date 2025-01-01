# -*- coding: utf-8 -*-
import copy

from vsg import parser
from vsg.token import sensitivity_list as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import name


def classify(iToken, lObjects):
    """
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    """

    iCurrent = iToken
    iStop = len(lObjects) - 1
    iOpenParenthesis = 0
    iCloseParenthesis = 0
    while iCurrent < iStop:
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        if utils.token_is_open_parenthesis(iCurrent, lObjects):
            iOpenParenthesis += 1
        if utils.token_is_close_parenthesis(iCurrent, lObjects):
            iCloseParenthesis += 1
        if iOpenParenthesis < iCloseParenthesis:
            break
        else:
            if utils.is_next_token(",", iCurrent, lObjects):
                utils.assign_token(lObjects, iCurrent, token.comma)
            else:
                iCurrent = name.classify_until([","], iCurrent, lObjects)
    return iCurrent


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
