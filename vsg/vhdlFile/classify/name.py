# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import direction
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import external_name


def classify_until(lUntils, iToken, lObjects, oType=parser.todo):
    """
      name ::=
              simple_name
            | operator_symbol
            | character_literal
            | selected_name
            | indexed_name
            | slice_name
            | attribute_name
            | external_name

    NOTE: At the moment, everything will be set to parser.todo.
    """

    iReturn = external_name.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

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
        elif lObjects[iCurrent].get_lower_value() in lUntils:
            break
        else:
            utils.assign_special_tokens(lObjects, iCurrent, oType)
    return iCurrent
