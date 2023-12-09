
from vsg import parser

from vsg.vhdlFile import utils

from vsg.vhdlFile.classify import range
from vsg.vhdlFile.classify import subtype_indication


def detect(iToken, lObjects):
    '''
    discrete_range ::=
        *discrete*_subtype_indication | range
    '''
    if utils.are_next_consecutive_tokens([None, '(', None, ')'], iToken, lObjects):
        return subtype_indication.classify(iToken, lObjects)
    return range.detect(iToken, lObjects)


def classify(iToken, lObjects):
    '''
    discrete_range ::=
        *discrete*_subtype_indication | range
    '''

    return utils.assign_token(lObjects, iToken, parser.todo)


def classify_until(lUntils, iToken, lObjects):
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
        elif iOpenParenthesis == iCloseParenthesis:
            if lObjects[iCurrent].get_lower_value() in lUntils:
                break
            else:
                utils.assign_token(lObjects, iCurrent, parser.todo)
        else:
            utils.assign_token(lObjects, iCurrent, parser.todo)
    return iCurrent
