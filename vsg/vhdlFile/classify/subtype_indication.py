
from vsg import parser

from vsg.vhdlFile import utils

from vsg.token import direction
from vsg.token.ieee.std_logic_1164 import types


def classify(iToken, lObjects):
    '''
    subtype_indication ::=
        [ resolution_indication ] type_mark [ constraint ]
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
            elif sValue.lower() == 'std_logic_vector':
                utils.assign_token(lObjects, iCurrent, types.std_logic_vector)
            elif sValue.lower() == 'std_ulogic_vector':
                utils.assign_token(lObjects, iCurrent, types.std_ulogic_vector)
            elif sValue.lower() == 'std_ulogic':
                utils.assign_token(lObjects, iCurrent, types.std_ulogic)
            elif sValue.lower() == 'std_logic':
                utils.assign_token(lObjects, iCurrent, types.std_logic)
            elif sValue.lower() == 'integer':
                utils.assign_token(lObjects, iCurrent, types.integer)
            elif sValue.lower() == 'signed':
                utils.assign_token(lObjects, iCurrent, types.signed)
            elif sValue.lower() == 'unsigned':
                utils.assign_token(lObjects, iCurrent, types.unsigned)
            elif sValue.lower() == 'natural':
                utils.assign_token(lObjects, iCurrent, types.natural)

            else:
                utils.assign_token(lObjects, iCurrent, oType)
    return iCurrent
