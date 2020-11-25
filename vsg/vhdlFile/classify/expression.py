
from vsg import parser

from vsg.vhdlFile import utils


def classify(iToken, lObjects):
    '''
    expression ::=
        condition_operator primary
      | logical_expression
    '''
    return utils.assign_token(lObjects, iToken, parser.todo)


def classify_until(lUntils, iToken, lObjects):
    iEnd = len(lObjects) - 1
    iCurrent = iToken
    iOpenParenthesis = 0
    iCloseParenthesis = 0
    for iIndex in range(iToken, len(lObjects)):
        if not utils.is_item(lObjects, iIndex):
            continue
        if utils.token_is_open_parenthesis(iIndex, lObjects):
           iOpenParenthesis += 1
        if utils.token_is_close_parenthesis(iIndex, lObjects):
           iCloseParenthesis += 1
        if iOpenParenthesis < iCloseParenthesis:
            break
        elif lObjects[iIndex].get_value().lower() in lUntils:
            if iOpenParenthesis == iCloseParenthesis:
                break
        else:
            utils.assign_token(lObjects, iIndex, parser.todo)
        if iCurrent == iEnd:
            return iToken
    return iCurrent
