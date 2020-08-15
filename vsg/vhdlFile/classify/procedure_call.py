
from vsg import parser

from vsg.token import procedure_call as token

from vsg.vhdlFile.classify import actual_parameter_part

iOpenParenthesis = 0
iCloseParenthesis = 0


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    procedure_call ::= *procedure*_name [ ( actual_parameter_part ) ]
    '''

#    if not dVars['procedure_call']['procedure_name']:
#
#        if classify_procedure_name(oObject, iObject, lObjects, dVars):
#            return True
#
#    else:

    if not dVars['procedure_call']['open_parenthesis']:

        if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
            return True

    else:

        update_parenthesis_counts(oObject, iOpenParenthesis, iCloseParenthesis)

        if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
            return True
    
        if actual_parameter_part.tokenize(oObject, iObject, lObjects, dVars):
            return True

    return False



def classify_procedure_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item and oObject.get_value().lower() != 'end':
        lObjects[iObject] = token.procedure_name(oObject.get_value())
        dVars['procedure_call']['procedure_name'] = True
        return True
    return False


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        iOpenParenthesis = 1
        iCloseParenthesis = 0
        dVars['procedure_call']['open_parenthesis'] = True
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        if iOpenParenthesis == iCloseParenthesis:
            lObjects[iObject] = token.close_parenthesis()
            clear_flags(dVars)
            return True
    return False


def clear_flags(dVars):
    actual_parameter_part.clear_flags(dVars)
    dVars['procedure_call']['procedure_name'] = False
    dVars['procedure_call']['open_parenthesis'] = False


def update_parenthesis_counts(oObject, iOpenParenthesis, iCloseParenthesis):
    if oObject.get_value() == '(':
        iOpenParenthesis += 1
    if oObject.get_value() == ')':
        iCloseParenthesis += 1
