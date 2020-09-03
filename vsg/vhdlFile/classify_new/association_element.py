
from vsg.token import association_element as token

from vsg.vhdlFile import utils

'''
    association_element ::=
        [ formal_part => ] actual_part
'''

def detect(iCurrent, lObjects):
    '''
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

    iToken = iStart

    # Classify formal part if it exists
    if utils.find_in_range('=>', iStart, sEnd, lObjects):
        iFormalStart, iFormalEnd = utils.get_range(lObjects, iStart, '=>')
        for iToken in range(iFormalStart, iFormalEnd + 1):
            if utils.is_item(lObjects, iToken):
                if utils.classify_token('=>', token.assignment, iToken, lObjects):
                    continue
                else:
                    utils.assign_token(lObjects, iToken, token.formal_part)

    # Classify actual part
    for iToken in range(iToken, iEnd):
        if utils.is_item(lObjects, iToken):
            utils.assign_token(lObjects, iToken, token.actual_part)

    return iToken
