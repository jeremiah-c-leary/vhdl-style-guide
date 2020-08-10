
from vsg import parser

from vsg.vhdlFile.classify import subprogram_header
from vsg.vhdlFile.classify import formal_parameter_list

from vsg.token import procedure_specification as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    procedure_specification ::=
        procedure designator
            subprogram_header
            [ [ parameter ] ( formal_parameter_list ) ]
    '''
    if not dVars['procedure_specification']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['procedure_specification']['designator']:
        
            if classify_designator(oObject, iObject, lObjects, dVars):
                return True

        else:

            if not dVars['procedure_specification']['open_parenthesis']:

                if subprogram_header.tokenize(oObject, iObject, lObjects, dVars):
                    return True
            
                if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                    return True
    
                if classify_parameter_keyword(oObject, iObject, lObjects, dVars):
                    return True

            else:

                update_parenthesis_counts(oObject, dVars)

                if not dVars['procedure_specification']['close_parenthesis']:
    
                    if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                        return True

                    if formal_parameter_list.tokenize(oObject, iObject, lObjects, dVars):
                        return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'procedure':
        lObjects[iObject] = token.keyword(sValue)
        dVars['procedure_specification']['keyword'] = True
        return True
    return False


def classify_designator(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.designator(sValue)
        dVars['procedure_specification']['designator'] = True
        return True
    return False


def classify_parameter_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'parameter':
        lObjects[iObject] = token.parameter_keyword(sValue)
        return True
    return False


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        dVars['iOpenParenthesisCount'] = 1
        dVars['iCloseParenthesisCount'] = 0
        dVars['procedure_specification']['open_parenthesis'] = True
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        lObjects[iObject] = token.close_parenthesis()
        if dVars['iOpenParenthesisCount'] == dVars['iCloseParenthesisCount']:        
            dVars['procedure_specification']['close_parenthesis'] = True
            return True
    return False


def clear_flags(dVars):
    subprogram_header.clear_flags(dVars)
    formal_parameter_list.clear_flags(dVars)
    dVars['procedure_specification'] = {}
    dVars['procedure_specification']['keyword'] = False
    dVars['procedure_specification']['designator'] = False
    dVars['procedure_specification']['open_parenthesis'] = False
    dVars['procedure_specification']['close_parenthesis'] = False


def update_parenthesis_counts(oObject, dVars):
    if oObject.get_value() == '(':
        dVars['iOpenParenthesisCount'] += 1
    if oObject.get_value() == ')':
        dVars['iCloseParenthesisCount'] += 1

