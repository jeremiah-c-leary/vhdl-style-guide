
from vsg.token import association_element as token

from vsg.vhdlFile import utils


def detect(iCurrent, lObjects):
    '''
    association_element ::=
        [ formal_part => ] actual_part

    An association element will either end in a close parenthesis or a comma that is not within paranthesis.

    accociation_element [)|,]

    '''
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
            classify(iCurrent, iToken, lObjects, ')')
            return iToken
        if iCloseParenthesis == iOpenParenthesis:
            if utils.token_is_comma(iToken, lObjects):
                classify(iCurrent, iToken, lObjects, ',')
                return iToken
        iToken += 1
    return iToken


def classify(iStart, iEnd, lObjects, sEnd):
    iCurrent = iStart
    sPrint = ''
    for oObject in lObjects[iStart:iEnd + 1]:
        sPrint += oObject.get_value()
    # Classify formal part if it exists
    if utils.find_in_index_range('=>', iStart, iEnd, lObjects):
        iCurrent = utils.assign_tokens_until('=>', token.formal_part, iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required('=>', token.assignment, iCurrent, lObjects)

    # Classify actual part
    for iCurrent in range(iCurrent, iEnd):
        if utils.is_item(lObjects, iCurrent):
            utils.assign_token(lObjects, iCurrent, token.actual_part)

    return iCurrent
