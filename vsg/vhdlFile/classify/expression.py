
from vsg import parser

from vsg.vhdlFile import utils

from vsg.token import direction


def classify(iToken, lObjects):
    '''
    expression ::=
        condition_operator primary
      | logical_expression
    '''
    return utils.assign_token(lObjects, iToken, parser.todo)


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
#        print(f'{lObjects[iCurrent].get_value()} | {iOpenParenthesis} | {iCloseParenthesis} | {lUntils}')
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
            sValue = lObjects[iCurrent].get_value()
            if sValue == ')':
                utils.assign_token(lObjects, iCurrent, parser.close_parenthesis)
            elif sValue == '(':
                utils.assign_token(lObjects, iCurrent, parser.open_parenthesis)
            elif sValue == '-':
                utils.assign_token(lObjects, iCurrent, parser.todo)
            elif sValue == '+':
                utils.assign_token(lObjects, iCurrent, parser.todo)
            elif sValue == '*':
                utils.assign_token(lObjects, iCurrent, parser.todo)
            elif sValue == '**':
                utils.assign_token(lObjects, iCurrent, parser.todo)
            elif sValue == '/':
                utils.assign_token(lObjects, iCurrent, parser.todo)
            elif sValue.lower() == 'downto':
                utils.assign_token(lObjects, iCurrent, direction.downto)
            elif sValue.lower() == 'to':
                utils.assign_token(lObjects, iCurrent, direction.to)
            else:
                utils.assign_token(lObjects, iCurrent, oType)
    return iCurrent


def classify_until_old(lUntils, iToken, lObjects):
    iEnd = len(lObjects) - 1
    iCurrent = iToken
    iOpenParenthesis = 0
    iCloseParenthesis = 0
    for iIndex in range(iToken, len(lObjects)):
        print(lObjects[iIndex].get_value())
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
