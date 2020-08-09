
from vsg import parser
from vsg.token import enumeration_type_definition as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    enumeration_type_definition ::=
        ( enumeration_literal { , enumeration_literal } )
    ''' 

    if not dVars['type_declaration']['enumeration_type_declaration']['open_parenthesis']:

        if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
            return True 

        if classify_comma(oObject, iObject, lObjects, dVars):
            return True 

        if classify_enumeration_literal(oObject, iObject, lObjects, dVars):
            return True 

    return False


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == '(':
        lObjects[iObject] = token.open_parenthesis()
        dVars['type_declaration']['enumeration_type_declaration']['open_parenthesis'] = True 
        return True
    return False


def classify_comma(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ',':
        lObjects[iObject] = token.comma()
        return True
    return False


def classify_enumeration_literal(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.enumeration_literal(oObject.get_value())
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ')':
        lObjects[iObject] = token.close_parenthesis()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['type_declaration']['enumeration_type_declaration']['open_parenthesis'] = False
