
from vsg.vhdlFile.classify import subprogram_header
from vsg.vhdlFile.classify import formal_parameter_list

from vsg.token import function_specification as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    function_specification ::=
        [ pure | impure ] function designator
            subprogram_header
            [ [ parameter ] ( formal_parameter_list ) ] return type_mark
    '''
    if not dVars['function_specification']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['function_specification']['designator']:
        
            if classify_keyword(oObject, iObject, lObjects, dVars):
                return True

            if classify_pure_keyword(oObject, iObject, lObjects, dVars):
                return True

            if classify_impure_keyword(oObject, iObject, lObjects, dVars):
                return True

        else:

            if not dVars['function_specification']['open_parenthesis']:

                if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                    return True
    
                if classify_parameter_keyword(oObject, iObject, lObjects, dVars):
                    return True

                if subprogram_header.tokenize(oObject, iObject, lObjects, dVars):
                    return True
            
            else:

                if not dVars['function_specification']['close_parenthesis']:

                    if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                        return True
        
                    if formal_parameter_list.tokenize(oObject, iObject, lObjects, dVars):
                        return True

            if not dVars['function_specification']['return']:

                if classify_return_keyword(oObject, iObject, lObjects, dVars):
                    return True

            else:        

                if classify_type_mark(oObject, iObject, lObjects, dVars):
                    return True
        

    return False


def classify_pure_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'pure':
        lObjects[iObject] = token.pure_keyword(sValue)
        return True
    return False


def classify_impure_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'impure':
        lObjects[iObject] = token.impure_keyword(sValue)
        return True
    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'function':
        lObjects[iObject] = token.keyword(sValue)
        dVars['function_specification']['keyword'] = True
        return True
    return False


def classify_designator(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.designator(sValue)
        dVars['function_specification']['designator'] = True
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
        dVars['function_specification']['open_parenthesis'] = True
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.close_parenthesis()
        dVars['function_specification']['close_parenthesis'] = True
        return True
    return False


def classify_return_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'return':
        lObjects[iObject] = token.return_keyword(sValue)
        dVars['function_specification']['return'] = True
        return True
    return False


def classify_type_mark(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.type_mark(sValue)
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['function_specification'] = {}
    dVars['function_specification']['keyword'] = False
    dVars['function_specification']['designator'] = False
    dVars['function_specification']['open_parenthesis'] = False
    dVars['function_specification']['return'] = False
