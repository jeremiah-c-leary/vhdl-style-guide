
from vsg import parser

from vsg.vhdlFile import utils

from vsg.token import direction


def classify_until(lUntils, iToken, lObjects, oType=parser.todo):
    '''
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
