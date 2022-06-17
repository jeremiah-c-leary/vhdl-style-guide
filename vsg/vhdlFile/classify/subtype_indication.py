
from vsg import parser

from vsg.vhdlFile import utils

from vsg.token import subtype_indication as token

from vsg.vhdlFile.classify import resolution_indication
from vsg.vhdlFile.classify import constraint


def classify(iToken, lObjects):
    '''
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
    '''

    iCurrent = resolution_indication.detect(iToken, lObjects)
    iCurrent = utils.find_next_non_whitespace_token(iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.type_mark, iCurrent, lObjects)
    iCurrent = constraint.detect(iCurrent, lObjects)
    return iCurrent


def classify_until(lUntils, iToken, lObjects, oType=parser.todo):
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
        elif lObjects[iCurrent].get_value().lower() in lUntils:
            if utils.token_is_close_parenthesis(iCurrent, lObjects):
                if iOpenParenthesis == iCloseParenthesis:
                    utils.assign_token(lObjects, iCurrent, parser.close_parenthesis)
                    continue
                else:
                    break
            elif utils.token_is_comma(iCurrent, lObjects):
                if iOpenParenthesis == iCloseParenthesis:
                    break
                else:
                    utils.assign_token(lObjects, iCurrent, parser.comma)
            else:
                break
        else:
            utils.assign_special_tokens(lObjects, iCurrent, oType)
    return iCurrent
