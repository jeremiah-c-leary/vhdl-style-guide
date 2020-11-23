
from vsg import parser

from vsg.token import sensitivity_list as token

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
    '''

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
            if utils.is_next_token(',', iCurrent, lObjects):
                utils.assign_token(lObjects, iCurrent, token.comma)
            else:
                utils.assign_token(lObjects, iCurrent, parser.todo)
    return iCurrent


def classify_until(lUntils, iToken, lObjects):
    '''
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    '''

    iCurrent = iToken
    iLast = 0
    while iLast != iCurrent:
        iLast = iCurrent
        if lObjects[utils.find_next_token(iCurrent, lObjects)].get_value().lower() in lUntils:
            return iCurrent
        iCurrent = utils.assign_next_token_if(',', token.comma, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(parser.todo, iCurrent, lObjects)
