# -*- coding: utf-8 -*-

from vsg.token import association_element as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import formal_part


def detect(iCurrent, lObjects):
    """
    association_element ::=
        [ formal_part => ] actual_part

    An association element will either end in a close parenthesis or a comma that is not within parenthesis.

    association_element [)|,]

    """
    iOpenParenthesis = 0
    iCloseParenthesis = 0
    iToken = iCurrent
    while not utils.token_is_semicolon(iToken, lObjects):
        iToken = utils.find_next_token(iToken, lObjects)
        if utils.token_is_open_parenthesis(iToken, lObjects):
            iOpenParenthesis += 1
        if utils.token_is_close_parenthesis(iToken, lObjects):
            iCloseParenthesis += 1
        if iCloseParenthesis == iOpenParenthesis + 1:
            classify(iCurrent, iToken, lObjects, ")")
            return iToken
        if iCloseParenthesis == iOpenParenthesis:
            if utils.token_is_comma(iToken, lObjects):
                classify(iCurrent, iToken, lObjects, ",")
                return iToken
        iToken += 1
    return iToken


def classify(iStart, iEnd, lObjects, sEnd):
    iCurrent = iStart
    # Classify formal part if it exists
    if formal_part_detected(iStart, iEnd, lObjects):
        iCurrent = formal_part.classify(token.formal_part, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required("=>", token.assignment, iCurrent, lObjects)

    # Classify actual part
    for iCurrent in range(iCurrent, iEnd):
        if utils.is_item(lObjects, iCurrent):
            utils.assign_token(lObjects, iCurrent, token.actual_part)

    return iCurrent


def formal_part_detected(iStart, iEnd, lObjects):
    iParen = 0
    for iIndex in range(iStart, iEnd):
        iParen = utils.update_paren_counter(iIndex, lObjects, iParen)
        if iParen == 0 and utils.object_value_is(lObjects, iIndex, "=>"):
            return True
    return False
